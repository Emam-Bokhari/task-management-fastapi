from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schema.blog_schema import BlogCreate, BlogCreateResponse
from app.services.blog_service import BlogService

router = APIRouter(tags=["Blogs"])


def get_blog_service(db: Annotated[Session, Depends(get_db)]) -> BlogService:
    """Dependency to get blog service"""
    return BlogService(db=db)


@router.post(
    "",
    response_model=BlogCreateResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new blog",
)
@router.post("/", response_model=BlogCreateResponse, include_in_schema=False)
def create_blog(
    payload: BlogCreate,
    blog_service: Annotated[BlogService, Depends(get_blog_service)],
):
    """Create a new blog entry"""
    return blog_service.create_blog(payload)
