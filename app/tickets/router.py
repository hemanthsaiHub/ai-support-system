from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.database.models import Ticket
from app.tickets.schemas import TicketCreate
from app.auth.dependencies import get_current_user
from app.ai.utils import analyze_sentiment, categorize_ticket, generate_ai_reply

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.post("/create")
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    sentiment = analyze_sentiment(ticket.description)
    category = categorize_ticket(ticket.description)
    ai_reply = generate_ai_reply(sentiment, category)

    new_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        priority=ticket.priority,
        category=category,
        sentiment=sentiment,
        ai_reply=ai_reply,
        user_id=current_user["user_id"]
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket