from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine, Base
from app.routers.auth import router as auth_routers
from app.routers.products import router as products
from app.routers.admin import router as admin
from app.models.product import Product
from app.models.users import User
from app.models.order import Order, OrderItem
from app.models.cart import CartItems
app = FastAPI(title='api shop mobile', version='1.0.0')

app.include_router(auth_routers)
app.include_router(products)
app.include_router(admin)


@app.on_event('startup')
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get('/')
def root():
    return {'message': 'welcome to shop api'}


@app.get("/db-test")
def db_test():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        return {"database": result.scalar()}
