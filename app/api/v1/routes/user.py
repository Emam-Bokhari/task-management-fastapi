from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies import get_current_user, get_db
from app.models.user import UserModel
from app.schema.user_schema import (
    AccessTokenSchema,
    LoginSchema,
    RegisterResponseSchema,
    UserResponseSchema,
    UserSchema,
)
from app.services.user_service import UserService

router = APIRouter(tags=["Users"])


def get_user_service(db: Annotated[Session, Depends(get_db)]) -> UserService:
    """Dependency to get user service"""
    return UserService(db=db)


@router.post(
    "/register",
    response_model=RegisterResponseSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
def register_user(
    payload: UserSchema,
    user_service: Annotated[UserService, Depends(get_user_service)],
) -> RegisterResponseSchema:
    """Register a new user with email and password"""
    return user_service.register_user(payload)


@router.post(
    "/login",
    response_model=AccessTokenSchema,
    status_code=status.HTTP_200_OK,
    summary="User login",
)
def login_user(
    payload: LoginSchema,
    user_service: Annotated[UserService, Depends(get_user_service)],
):
    """Authenticate a user and return a JWT access token"""
    return user_service.login_user(payload)


@router.get(
    "/me",
    response_model=UserResponseSchema,
    summary="Get current user profile",
)
def get_current_user_profile(
    current_user: Annotated[UserModel, Depends(get_current_user)],
):
    """Get the currently authenticated user's profile"""
    return current_user
