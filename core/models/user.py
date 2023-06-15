from sqlalchemy import Column, Integer, PrimaryKeyConstraint, String

from core.config.database import Base


class User(Base):
    __tablename__ = "user"

    username = Column(String, primary_key=True, nullable=False)
    password = Column(String, nullable=False)
