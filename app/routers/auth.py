from fastapi import APIRouter
from app.utils.auth import create_token

router = APIRouter(tags=["Auth"])

@router.post("/login")
def login():
    return {
        "access_token": create_token({"user": "admin"}),
        "token_type": "bearer"
    }