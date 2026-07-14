from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.users import User
from app.schemas.user import UserCreate, UserLogin
from app.utils.security import hash_password, verify_password, create_accsess_token


def register_user(user_data: UserCreate, db: Session):
    register = db.query(User).filter(
        User.username == user_data.username | User.email == user_data.email
    ).first()
    if register:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='کاربر موجود است لطفا وارد شوید'
        )

    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    token = create_accsess_token(
        data={"sub": str(user.id), "is_admin": user.is_admin})
    return {"access_token": token, "token_type": "bearer"}


def login_user(db: Session, user_data: UserLogin) -> dict:
    user = db.query(User).filter(User.username == user_data.username).first()
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="نام کاربری یا رمز عبور اشتباه است",
        )

    token = create_accsess_token(
        data={"sub": str(user.id), "is_admin": user.is_admin})
    return {"access_token": token, "token_type": "bearer"}
