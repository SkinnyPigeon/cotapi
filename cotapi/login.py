import os
from passlib.context import CryptContext
from user import UserPersistance as UP

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str):
    up = UP(username, password)
    user = up.load_user()
    if not user:
        return False
    if not verify_password(password, user.key):
        return False
    return user