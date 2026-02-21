from fastapi import FastAPI
from app.database.db import engine, Base
from app.auth.router import router as auth_router
from app.tickets.router import router as ticket_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Support System")

app.include_router(auth_router)
app.include_router(ticket_router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)