from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.product import Product
from app.schemas.products import ProductCreate, ProductUpdate


def create_product(db: Session, data: ProductCreate) -> Product:
    product = Product(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_all_products(db: Session) -> list[Product]:
    return db.query(Product).filter(Product.is_available == True).all()


def get_product_by_id(db: Session, product_id: int) -> Product:
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    return product


def update_product(db: Session, product_id: int, data: ProductUpdate) -> Product:
    product = get_product_by_id(db, product_id)
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int) -> None:
    product = get_product_by_id(db, product_id)
    db.delete(product)
    db.commit()
