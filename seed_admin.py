from sqlalchemy.orm import Session
from models import Users
from passlib.context import CryptContext
import os
from dotenv import load_dotenv

load_dotenv()

pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")
ADMIN_EMAIL=os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD=os.getenv("ADMIN_PASSWORD")

def create_admin(db: Session):

    admin = db.query(Users).filter(Users.email == ADMIN_EMAIL).first()

    if admin:
        print("Admin already exists")
        return

    hashed_pw = pwd.hash(ADMIN_PASSWORD)

    new_admin = Users(
        name="Admin",
        email=ADMIN_EMAIL,
        password=hashed_pw,
        role="admin"
    )

    db.add(new_admin)
    db.commit()

    print("Admin Created")