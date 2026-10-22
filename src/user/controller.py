from src.user.dtos import UserSchema
from sqlalchemy.orm import Session 

def register_user(payload:UserSchema,db:Session):
    return {"success":True}