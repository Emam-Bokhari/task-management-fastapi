from typing import Annotated, List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schema.product_schema import ProductCreate, ProductResponseSchema
from app.services.product_service import ProductService

router = APIRouter(tags=["Products"])


def get_product_service(db: Annotated[Session, Depends(get_db)]) -> ProductService:
    """Dependency to get product service"""
    return ProductService(db=db)


@router.post(
    "",
    response_model=ProductResponseSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new product",
)
@router.post("/", response_model=ProductResponseSchema, include_in_schema=False)
def create_product(
    payload: ProductCreate,
    product_service: Annotated[ProductService, Depends(get_product_service)],
):
    """Create a new product"""
    return product_service.create_product(payload)


@router.get(
    "",
    response_model=List[ProductResponseSchema],
    status_code=status.HTTP_200_OK,
    summary="List all products",
)
@router.get("/", response_model=List[ProductResponseSchema], include_in_schema=False)
def get_products(
    product_service: Annotated[ProductService, Depends(get_product_service)],
):
    """Retrieve all products"""
    return product_service.get_products()
