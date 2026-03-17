#register user
from fastapi import HTTPException,Depends
from db import get_db
from models import Users
from sqlalchemy.orm import Session
from schema import UserReg
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def reg(user: UserReg, db: Session = Depends(get_db)):

    existing_user = db.query(Users).filter(Users.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=409, detail="Email already registered")

    hash_password = pwd_context.hash(user.password)

    new_user = Users(
        name=user.name,
        email=user.email,
        password=hash_password,
        role="user"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message":"registration successful",
        "email":new_user.email,
    }