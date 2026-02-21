from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.tickets.router import router as ticket_router

app = FastAPI(title="AI Support System")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(ticket_router, prefix="/tickets", tags=["Tickets"])

@app.get("/")
def root():
    return {"status": "API running"}