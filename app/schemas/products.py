from pydantic import BaseModel
from datetime import datetime


class ProductCreate(BaseModel):
    name: str
    brand: str
    description: str | None = None
    price: int
    stock: int = 0
    image_url: str | None = None
    is_available: bool = True


class ProductUpdate(BaseModel):
    name: str | None = None
    brand: str | None = None
    description: str | None = None
    price: int | None = None
    stock: int | None = None
    image_url: str | None = None
    is_available: bool | None = None


class ProductResponse(BaseModel):
    id: int
    name: str
    brand: str
    description: str | None
    price: int
    stock: int
    image_url: str | None
    is_available: bool
    created_at: datetime

    model_config = {"from_attributes": True}
