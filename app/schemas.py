# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    model_config = {"from_attributes": True}   # allow ORM objects -> pydantic

class Token(BaseModel):
    access_token: str
    token_type: str
    model_config = {"from_attributes": True}

class PetBase(BaseModel):
    name: str
    species: str
    breed: Optional[str] = None
    age: Optional[int] = None
    price: Optional[float] = None
    location: Optional[str] = None
    description: Optional[str] = None

class PetCreate(PetBase):
    pass

class PetOut(PetBase):
    id: int
    owner_id: int
    model_config = {"from_attributes": True}
