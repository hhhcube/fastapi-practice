from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

from pydantic.types import conint
# Class representation of a Post extending Pydantic BaseModel
#  Does validation and schema for frontend to send to us
# e.g. title str, content str, category str, published or draft bool
# Python reads these models top down 

# Create different models for each of the dsifferent request
 

# A Pydantic mode for creating a post
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    



class PostCreate(PostBase):
    pass


    

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True




class Post(BaseModel):
    id: int
    created_at: datetime
    # title: str
    # content: str
    owner_id: int
    owner: UserOut        

    class Config:
        orm_mode = True



class PostOut(BaseModel):
    Post: Post
    votes: int
    # title: str
    # content: str
         

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None




class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # trying to figure out if this is a 0 or 1
