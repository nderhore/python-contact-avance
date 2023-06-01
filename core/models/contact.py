from sqlalchemy import String, Column, Integer, PrimaryKeyConstraint

from core.config.database import Base


class Contact(Base):
    __tablename__ = "contact"

    id = Column(Integer, autoincrement=True)
    nom = Column(String(40), nullable=False)
    prenom = Column(String(40), nullable=False)
    telephone = Column(String(10), nullable=False)
    mail = Column(String(40), nullable=False)

    __table_args__ = (PrimaryKeyConstraint('id'),)
