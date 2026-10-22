from src.product.dtos import ProductCreate
from src.product.dtos import ProductUpdate
from src.product.models import Product
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.utils.send_response import send_response

def create_product(payload:ProductCreate,db:Session):
    data=payload.model_dump()

    new_product=Product(
        name=data["name"],
        description=data["description"],
        price=data["price"]
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {
        "status_code":201,
        "success":True,
        "message": "Product is created successfully",
        "data":new_product
    }


def get_products(db:Session):
     data=db.scalars(select(Product)).all()

     return send_response(
          success=True,
          status_code=200,
          message="Products data are retrieved successfully",
          data=data
     )
