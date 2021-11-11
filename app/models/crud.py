from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import false
from . import models, schemas
from ..segurity import Oauth

#READ
def get_user(db: Session, user_id: int):
    return db.query(models.user).filter(models.user.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.user).offset(skip).limit(limit).all()

def get_user_by_username(db: Session, username: str):
    return db.query(models.user).filter(models.user.username == username).first()

#CREATE
def create_user(db: Session, user: schemas.user_create):
    passwd = Oauth.hashed_passwd(user.password.encode())
    db_user = models.user(username=user.username, password=passwd, name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
