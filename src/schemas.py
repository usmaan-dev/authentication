from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class PostBase(BaseModel):
    
    title: str
    body: str
    # published: bool = True
    # rating: Optional[float] = None
  
 

class CreatePost(PostBase):
    pass   

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class ShowUser(BaseModel):
    email: EmailStr
    id: int
    created_at: datetime
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    


















# class CreatePost(BaseModel):
#     title: str
#     body: str
#     published: bool = True
#     # rating: Optional[float] = None
    
# class UpdatePost(BaseModel):
#     title: str
#     body: str
#     published: bool