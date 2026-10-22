from fastapi import APIRouter, Depends, status
from src.product import controller
from src.product.dtos import ProductCreate, ProductUpdate, ProductResponseSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session
from typing import List

routes=APIRouter(prefix="/api/v1")

@routes.post("/products",response_model=ProductResponseSchema, status_code=status.HTTP_201_CREATED)
def create_product(payload:ProductCreate,db:Session=Depends(get_db)):
    return controller.create_product(payload,db)

@routes.get("/products",response_model=List[ProductResponseSchema],status_code=status.HTTP_200_OK)
def get_products(db=Depends(get_db)):
    return controller.get_products(db)