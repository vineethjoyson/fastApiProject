
from pydantic import BaseModel
from typing import List

class Post(BaseModel):
    id: int
    title: str
    body: str

class User(BaseModel):
    id: int
    name: str
    email: str
    posts: List[Post]

class ResponseModel(BaseModel):
    users: List[User]
