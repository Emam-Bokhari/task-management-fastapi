from src.user.dtos import UserSchema
from sqlalchemy.orm import Session 
from src.user.models import UserModel

def register_user(payload:UserSchema,db:Session):
    
    return {"success":True}