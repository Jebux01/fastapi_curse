from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Avinushe32@localhost:3306/users"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()