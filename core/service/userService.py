import datetime
from http.client import HTTPException
from typing import Annotated

from fastapi import Depends
from jose import jwt, JWTError
from jose.constants import ALGORITHMS
from sqlalchemy.orm import Session
from starlette import status

from core.config.database import get_db
from core.config.security import EXPIRE_TIME_IN_SECOND, SECRET, authentication_mode
from core.models.user import User
from core.schema.tokenSchema import TokenData


async def get_user(username: str, db: Session = Depends(get_db)) -> User:
    return db.query(User).filter(User.username == username).first()


def create_token(data: dict):
    data["exp"] = data["iat"] + datetime.timedelta(seconds=EXPIRE_TIME_IN_SECOND)
    return jwt.encode(claims=data,
                      key=SECRET)


# retrouver l'utilisateur qui possède le token donné
def current_active_user(token: Annotated[str, Depends(authentication_mode)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload: dict = jwt.decode(access_token=token,
                                   key=SECRET,
                                   algorithms=[ALGORITHMS.HS256])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(token_data.username)
    if user is None:
        raise credentials_exception
    return user
