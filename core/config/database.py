from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mariadb+mysqlconnector://nathand59_python:Josecestleboss@mysql-nathand59.alwaysdata.net"
                       "/nathand59_python_avance")

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
