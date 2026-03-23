
from fastapi import APIRouter
from app.schemas.auth_schema import LoginRequest, LoginResponse, TokenData
from app.services.auth_service import create_access_token, create_refresh_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=LoginResponse)
def login(credentials: LoginRequest) -> LoginResponse:
    # TODO: Validate credentials against database
    user_data = TokenData(sub=credentials.email, role="user")
    
    return LoginResponse(
        access_token=create_access_token(user_data.dict()),
        refresh_token=create_refresh_token(user_data.dict())
    )
