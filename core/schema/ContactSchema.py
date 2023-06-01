from pydantic import BaseModel


class ContactBase(BaseModel):
    nom: str
    prenom: str
    telephone: str
    mail: str


class ContactUpdate(ContactBase):
    id: int


class ContactCreate(ContactBase):
    pass


class Contact(ContactBase):
    class Config:
        orm_mode = True
