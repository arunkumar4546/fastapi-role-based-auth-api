# ---------------- Model ----------------
from db import Base
from sqlalchemy import Column,Integer,String

class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role= Column(String,default="user")