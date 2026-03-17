# ---------------- Schema ----------------

from pydantic import BaseModel,EmailStr,Field

class UserReg(BaseModel):
    name: str
    email: EmailStr
    password: str=Field(min_length=6,max_length=12)

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str