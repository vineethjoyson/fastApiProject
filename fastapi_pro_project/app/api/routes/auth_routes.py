
from fastapi import APIRouter
from app.services.auth_service import create_access_token, create_refresh_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login():
    user = {"sub": "test@example.com", "role": "admin"}
    return {
        "access_token": create_access_token(user),
        "refresh_token": create_refresh_token(user)
    }
