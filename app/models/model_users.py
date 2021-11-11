from pydantic import BaseModel, validator
from typing import Optional

class user(BaseModel):
    username: str
    password: str
    name: str
    age: int
    profession: Optional[str] = 'Developer'

    #decorador
    # @validator('*')
    # def empty_values(cls, v):
    #     if len(v) == 0:
    #         raise ValueError('Es necesario mandar toda la informacion requerida')
    #     return v.title()

    @validator('password')
    def validate_password(cls, v):
        if len(v) == 0:
            raise ValueError('Es necesario un password')
        return v.title()