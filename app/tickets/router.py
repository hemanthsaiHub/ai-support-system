from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter()


class TicketCreate(BaseModel):
    title: str
    description: str


@router.post("/create")
def create_ticket(ticket: TicketCreate):
    return {
        "message": "Ticket created",
        "ticket": ticket
    }