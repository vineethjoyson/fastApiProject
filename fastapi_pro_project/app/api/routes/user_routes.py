
from fastapi import APIRouter, Depends
from app.dependencies.auth import verify_token
from app.services.user_service import get_users_with_posts
from app.schemas.user_schema import UsersListResponse, UserResponse, UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/details", response_model=UsersListResponse)
async def get_details(user=Depends(verify_token)) -> UsersListResponse:
    """Get all users with their posts (requires authentication)"""
    return await get_users_with_posts()


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, user=Depends(verify_token)) -> UserResponse:
    """Get a specific user by ID"""
    # TODO: Implement get_user service
    pass


@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(user_data: UserCreate, user=Depends(verify_token)) -> UserResponse:
    """Create a new user"""
    # TODO: Implement create_user service
    pass


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_data: UserUpdate, user=Depends(verify_token)) -> UserResponse:
    """Update a user"""
    # TODO: Implement update_user service
    pass


@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int, user=Depends(verify_token)):
    """Delete a user"""
    # TODO: Implement delete_user service
    pass
