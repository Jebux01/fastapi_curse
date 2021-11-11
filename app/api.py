# pip3 install SQLAlchemy, FastAPI, Virtualenv, pymysql

from datetime import timedelta
from typing import final, List

from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import ReturnTypeFromArgs, user
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from .models import model_users, models, schemas, crud
from .segurity import Oauth
from .db import session_local, engine

models.base.metadata.create_all(bind=engine)


ACCESS_TOKEN_EXPIRE_MINUTES = 30

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    }
]

app = FastAPI(
    title="Kabbalah Interactive",
    description="API to manage users",
    version="1.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Christian Gutierrez",
        "url": "http://x-force.example.com/contact/",
        "email": "jebux@xxxx.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)

aouth2_schem = OAuth2PasswordBearer(tokenUrl="token")

origins = [
    "http://localhost",
    "http://localhost:52333",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()



@app.get("/getusers", response_model=List[schemas.user], tags=['users'])
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.post("/createuser", response_model=schemas.user, tags=['users'])
async def create_user(user: schemas.user_create, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login")
async def login(user: schemas.login_data, db: Session = Depends(get_db)):
    user = Oauth.authenticate_user(db, username=user.username, password=user.password)
    return 
    
@app.post("/token", response_model=schemas.token)
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = Oauth.authenticate_user(db, username=form_data.username, password=form_data.password)
    print(user.username)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data_encode = {"sub": user.username}
    print(data_encode)
    access_token = Oauth.create_access_token(data=data_encode, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}