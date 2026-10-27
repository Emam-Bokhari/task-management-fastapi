from datetime import datetime, timedelta, timezone
from typing import Any
import jwt
from fastapi import HTTPException, status
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.user import UserModel
from app.schema.user_schema import LoginSchema, UserSchema

password_hash = PasswordHash.recommended()


def get_password_hash(password: str) -> str:
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


def create_access_token(user: UserModel) -> str:
    exp_time = datetime.now(timezone.utc) + timedelta(
        seconds=settings.ACCESS_TOKEN_EXPIRE_SECONDS
    )
    jwt_payload = {
        "sub": str(user.id),
        "user_name": user.user_name,
        "exp": exp_time,
    }
    return jwt.encode(
        jwt_payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def verify_token(token: str) -> dict[str, Any]:
    try:
        return jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
            options={"require": ["sub", "exp"]},
        )
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        ) from None
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        ) from None


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def register_user(self, payload: UserSchema) -> dict[str, UserModel | str]:
        if self.db.query(UserModel).filter(UserModel.user_name == payload.user_name).first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This user name already exists, please select another user name",
            )

        normalized_email = payload.email.strip().lower()
        if self.db.query(UserModel).filter(UserModel.email == normalized_email).first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="This email is already registered",
            )

        new_user = UserModel(
            name=payload.name,
            user_name=payload.user_name,
            password=get_password_hash(payload.password),
            email=normalized_email,
            is_active=True,
            is_deleted=False,
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return {"token": create_access_token(new_user), "user": new_user}

    def login_user(self, payload: LoginSchema) -> dict[str, str]:
        user = self.db.query(UserModel).filter(UserModel.user_name == payload.user_name).first()

        if (
            not user
            or not verify_password(payload.password, user.password)
            or not user.is_active
            or user.is_deleted
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return {"access_token": create_access_token(user), "token_type": "bearer"}


def register_user(payload: UserSchema, db: Session):
    return UserService(db).register_user(payload)


def login_user(payload: LoginSchema, db: Session):
    return UserService(db).login_user(payload)
