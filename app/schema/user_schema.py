from pydantic import BaseModel, ConfigDict


class UserSchema(BaseModel):
    name: str
    user_name: str
    password: str
    email: str
    is_active: bool = True
    is_deleted: bool = False


class UserResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    user_name: str
    email: str
    is_active: bool
    is_deleted: bool


# UserPublic alias matching the reference project naming
UserPublic = UserResponseSchema


class LoginSchema(BaseModel):
    user_name: str
    password: str


class AccessTokenSchema(BaseModel):
    access_token: str
    token_type: str


class RegisterResponseSchema(BaseModel):
    token: str
    user: UserResponseSchema
