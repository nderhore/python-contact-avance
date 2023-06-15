from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

SECRET = "joseaimelesfrites"
EXPIRE_TIME_IN_SECOND = 3600


password_context = CryptContext(schemes=["bcrypt"])

authentication_mode = OAuth2PasswordBearer(tokenUrl="api/login")


def verify_password(plain_password: str, password_hash: str) -> bool:
    return password_context.verify(secret=plain_password, hash=password_hash)


def get_hash_password(plain_password: str) -> str:
    return password_context.hash(secret=plain_password)
