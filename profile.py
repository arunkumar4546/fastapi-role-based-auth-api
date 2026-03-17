#auth approve
from fastapi import Depends
from auth_handler import get_current_user

def get_profile(user = Depends(get_current_user)):
    return{
        "message":"Authorised",
        "user_name":user.name
    }