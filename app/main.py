from fastapi import FastAPI

from app.auth.router import router as auth_router
from app.tickets.router import router as tickets_router

app = FastAPI(
    title="AI Support System",
    version="1.0.0"
)

# Include routers (PREFIX ONLY HERE)
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(tickets_router, prefix="/tickets", tags=["Tickets"])


@app.get("/")
def root():
    return {"message": "AI Support System running"}