from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserLogin, Token
from app.auth.authen import register_user, login_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix='/api/auth', tags=["Auth"])


@router.post('/register', response_model=Token)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    return register_user(db=db, user_data=user_data)


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user_data = UserLogin(
        username=form_data.username,
        password=form_data.password,
    )
    return login_user(db=db, user_data=user_data)
