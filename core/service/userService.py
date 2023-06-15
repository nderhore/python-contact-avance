import datetime

from fastapi import Depends
from jose import jwt
from sqlalchemy.orm import Session

from core.config.database import get_db
from core.config.security import EXPIRE_TIME_IN_SECOND, SECRET
from core.models.user import User


def get_user(username : str, db : Session = Depends(get_db)) -> User:
    return db.query(User).filter(User.username == username).first()


def create_token(data : dict):
    data["exp"] = data["iat"] + datetime.timedelta(seconds=EXPIRE_TIME_IN_SECOND)
    return jwt.encode(claims=data,
                      key=SECRET)



