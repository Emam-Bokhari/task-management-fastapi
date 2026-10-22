from src.user.dtos import UserSchema
from sqlalchemy.orm import Session 
from src.user.models import UserModel
from fastapi import HTTPException
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def register_user(payload:UserSchema,db:Session):
    is_user=db.query(UserModel).filter(UserModel.user_name==payload.user_name).first()

    if is_user:
        raise HTTPException(
            status_code=400,
            detail="This user name is already exists, please select another user name"
        )

    is_user=db.query(UserModel).filter(UserModel.email==payload.email).first()
    
    if is_user:
        raise HTTPException(
            status_code=400,
            detail="This email is already exists, please try another email"
        )

    hash_password=get_password_hash(payload.password)

    new_user=UserModel(
        name=payload.name,
        user_name=payload.user_name,
        password=hash_password,
        email=payload.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user