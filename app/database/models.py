from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)

    status = Column(String, default="open")
    priority = Column(String, default="medium")
    category = Column(String, default="general")

    sentiment = Column(String, default="neutral")
    ai_reply = Column(Text)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")