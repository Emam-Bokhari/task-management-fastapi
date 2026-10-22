from fastapi import APIRouter, Depends
from src.product import controller
from src.product.dtos import ProductCreate, ProductUpdate
from src.utils.db import get_db
from sqlalchemy.orm import Session

routes=APIRouter(prefix="/api/v1")

@routes.post("/products")
def create_product(payload:ProductCreate,db:Session=Depends(get_db)):
    return controller.create_product(payload,db)

@routes.get("/products")
def get_products(db=Depends(get_db)):
    return controller.get_products(db)