from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    password: str


class UserUpdate(UserBase):
    pass


class UserCreate(UserBase):
    pass


class User(UserBase):
    class Config:
        orm_mode = True
