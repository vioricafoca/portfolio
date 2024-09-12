import uuid
from typing import Optional

from pydantic import BaseModel, EmailStr, Field

db_users = []

class BubbleUserCreate(BaseModel):
    firstName: str
    lastName: str
    gender: Optional[int]
    email: EmailStr
    bubbleId: str

    class Config:
        populate_by_name = True
        from_attributes = True


class BubbleUserUpdate(BaseModel):
    firstName: str
    lastName: str
    gender: int


class BubbleUserGet(BaseModel):
    id: uuid.UUID
    first_name: str = Field(alias='firstName')
    last_name: str = Field(alias='lastName')
    gender: int
    email: str
    bubble_id: str = Field(alias='bubbleId')

    class Config:
        populate_by_name = True
