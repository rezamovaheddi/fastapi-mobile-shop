from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import require_admin
from app.models.users import User
from app.schemas.products import ProductCreate, ProductUpdate, ProductResponse
from app.products.crud import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product,
)

router = APIRouter(prefix="/api/products", tags=["Products"])


@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return get_all_products(db)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return get_product_by_id(db, product_id)


@router.post("/", response_model=ProductResponse, status_code=201)
def create_new_product(data: ProductCreate, admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    return create_product(db, data)


@router.put("/{product_id}", response_model=ProductResponse)
def update_existing_product(product_id: int, data: ProductUpdate, admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    return update_product(db, product_id, data)


@router.delete("/{product_id}", status_code=204)
def delete_existing_product(product_id: int, admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    delete_product(db, product_id)
