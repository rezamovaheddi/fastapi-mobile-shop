from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import JWTError, jwt
from app.env import token

pwd_content = CryptContext(schemes=['bcrypt'], deprecated='auto')


def hash_password(password: str) -> str:
    return pwd_content.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_content.verify(password, hash=hashed_password)


def create_accsess_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, token, algorithm='H256')


def decode_access_token(tokens: str) -> dict | None:
    try:
        payload = jwt.decode(tokens, token, algorithms=['H256'])
        return payload
    except JWTError:
        return None
