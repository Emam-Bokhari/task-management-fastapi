from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schema.product_schema import ProductCreate


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, payload: ProductCreate) -> Product:
        data = payload.model_dump()
        new_product = Product(
            name=data["name"],
            description=data["description"],
            price=data["price"],
        )
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)
        return new_product

    def get_products(self) -> List[Product]:
        return list(self.db.scalars(select(Product)).all())


def create_product(payload: ProductCreate, db: Session) -> Product:
    return ProductService(db).create_product(payload)


def get_products(db: Session) -> List[Product]:
    return ProductService(db).get_products()
