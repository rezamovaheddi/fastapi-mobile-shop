from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Enum as SAEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum


class UserRol(enum.Enum):
    USER = 'user'
    ADMIN = 'admin'


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=50), index=True, nullable=False)
    email = Column(String(length=100), index=True, nullable=False)
    hashed_password = Column(String(150), index=True, nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now())

    cart_items = relationship("CartItems", back_populates="user")
    orders = relationship("Order", back_populates="user")

    # Email Verification

    is_verified = Column(Boolean, default=False)
    verification_code = Column(String(length=6), nullable=True)
    verification_expire = Column(DateTime, nullable=True)
