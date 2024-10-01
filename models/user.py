# models/user.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserSchema(BaseModel):
    name: str
    email: EmailStr

class UpdateUserModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@example.com"
            }
        }

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"]
    }
