from typing import Optional
from pydantic import BaseModel


class user_base(BaseModel):
    username: str


class user_create(BaseModel):
    username: str
    password: str
    name: str
    age: int


class user(user_base):
    name: str
    age: int
    profession: Optional[str] = 'Developer'

    class Config:
        orm_mode = True

class login_data(BaseModel):
    username: str
    password: str


class token(BaseModel):
    access_token: str
    token_type: str

class token_data(BaseModel):
    username: str