from pydantic import BaseModel, EmailStr
from typing import List, Optional


class PostResponse(BaseModel):
    id: int
    title: str
    body: str

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    posts: List[PostResponse] = []

    class Config:
        from_attributes = True


class UsersListResponse(BaseModel):
    users: List[UserResponse]

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
