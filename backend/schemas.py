from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class UserInDB(UserBase):
    id: int

    class Config:
        orm_mode = True
