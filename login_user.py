#login user
from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from models import Users
from schema import UserLogin
from db import get_db
from register_user import pwd_context
from auth_handler import token_create

def login(user: UserLogin, db: Session = Depends(get_db)):

    # 1️⃣ find student
    existing_user = db.query(Users).filter(Users.email == user.email).first()

    # 2️⃣ check user exists
    if not existing_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # 3️⃣ verify password
    if not pwd_context.verify(user.password, existing_user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # 4️⃣ ADD JWT TOKEN
    access_token=token_create(
        data={
            "id":existing_user.id,
            "role":existing_user.role
        }
    )

    # 5️⃣ return token
    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer"
    }