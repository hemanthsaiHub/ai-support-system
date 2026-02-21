from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class UserCreate(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


@router.post("/register")
def register(user: UserCreate):
    return {
        "message": "User registered successfully",
        "email": user.email
    }


@router.post("/login")
def login(user: UserLogin):
    if user.password != "admin":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "message": "Login successful",
        "token": "fake-jwt-token"
    }