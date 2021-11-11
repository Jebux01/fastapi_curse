from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# esta linea ira despues ya que esto es lo que nos ayudara a crear las relaciones
# from sqlalchemy.orm import relationship
from ..db import base

class user(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(100))
    name = Column(String(50))
    age = Column(Integer)
    profession = Column(String(50), default='Developer')

