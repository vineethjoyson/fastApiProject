
from fastapi import APIRouter, Depends
from app.dependencies.auth import verify_token
from app.services.user_service import get_users_with_posts

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/details")
async def get_details(user=Depends(verify_token)):
    return await get_users_with_posts()
