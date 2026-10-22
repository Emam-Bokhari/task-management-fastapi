from fastapi import APIRouter, Depends, status
from src.user.dtos import UserSchema
from src.user import controller
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.user.dtos import UserResponseSchema

routes=APIRouter(prefix="/api/v1")

@routes.post("/register")
def register_user(payload:UserSchema,response_model=UserResponseSchema,status_code=status.HTTP_201_CREATED,db:Session=Depends(get_db)):
    return controller.register_user(payload,db)
