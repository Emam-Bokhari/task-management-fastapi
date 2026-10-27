from pydantic import BaseModel, ConfigDict


class BlogCreate(BaseModel):
    name: str
    description: str
    price: int
    is_active: bool = True
    is_deleted: bool = False


class BlogCreateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str
    price: int
    is_active: bool
    is_deleted: bool
