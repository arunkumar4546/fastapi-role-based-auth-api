from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Users
from db import get_db
from schema import UserLogin, UserReg

from register_user import reg
from login_user import login

from auth_handler import get_current_user,get_admin

router = APIRouter()

# ---------------- Route ----------------
@router.post("/register")
def register(user:UserReg,db:Session = Depends(get_db)):
    return reg(user,db)

@router.post("/login")
def log(user:UserLogin,db:Session = Depends(get_db)):
    return login(user,db)

@router.get("/profile")
def profile(user = Depends(get_current_user)):
    return {
        "email":user.email,
        "name":user.name
    }

@router.get("/users")
def users(
    page : int = 1,
    limit : int = 5,
    admin:Users = Depends(get_admin), 
    db:Session = Depends(get_db)
):
    skip = (page - 1) * limit
    users = db.query(Users).offset(skip).limit(limit).all()

    return [
        {

            "name": user.name,
            "email": user.email,
            "role": user.role
        }
        for user in users
    ]

@router.get("/users/search")
def search_users(
    email: str | None = None,
    name: str | None = None,
    page: int = 1,
    limit: int = 5,
    admin: Users = Depends(get_admin),
    db: Session = Depends(get_db)
):
    
    query = db.query(Users)

    if email:
        query = query.filter(Users.email.contains(email))

    if name:
        query = query.filter(Users.name.contains(name))

    skip = (page - 1) * limit

    users = query.offset(skip).limit(limit).all()

    total = query.count()

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "role": user.role
            }
            for user in users
        ]
    }

@router.delete("/user/{id}")
def delete_user(id:int, admin:Users = Depends(get_admin), db:Session = Depends(get_db)):

    user = db.query(Users).filter(Users.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message":"User deleted"}

# @router.get("/test-error")
# def test_error():
#     raise Exception("Testing global exception handler")