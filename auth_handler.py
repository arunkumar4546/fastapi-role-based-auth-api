#---JWT TOKEN GENERATION

from jose import jwt
from datetime import datetime,timedelta
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
EXPIRE_TIME=30

def token_create(data:dict):
    to_encode = data.copy()
    expire=datetime.utcnow()+timedelta(EXPIRE_TIME)
    
    to_encode.update({"exp":expire})

    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

#JWT TOKEN MATCH CHECK

from jose import jwt,JWTError
from fastapi import Depends, HTTPException
from fastapi import Security
from fastapi.security import HTTPBearer
from db import get_db
from models import Users

security = HTTPBearer()
def get_current_user(credentials = Security(security),db = Depends(get_db)):

    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id = payload.get("id")

        if id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    
        user = db.query(Users).filter(Users.id == id).first()
        return user
    
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalid")
    
def get_admin(current_user:Users=Depends(get_current_user)):

    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only allowed")
    return current_user

