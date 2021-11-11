from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from .models import crud
from pydantic import BaseModel
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

class Oauth:
    @classmethod
    def authenticate_user(cls, db, username: str, password: str):
        user = crud.get_user_by_username(db, username)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        if not cls.verify_password(password, user.password):
            raise HTTPException(status_code=404, detail="Password Invalid")

        return user

    @classmethod
    def hashed_passwd(cls, plain_password):
        return pwd_context.hash(plain_password)

    @classmethod
    def verify_password(cls, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt 