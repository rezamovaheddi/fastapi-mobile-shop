from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine, Base
from app.routers.auth import router as auth_routers

app = FastAPI(title='api shop mobile', version='1.0.0')

app.include_router(auth_routers)


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
