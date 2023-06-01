from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.config.database import get_db
from core.models.contact import Contact
from core.schema.ContactSchema import ContactCreate
from core.schema.ContactSchema import Contact as contactPydantic

router = APIRouter()


@router.post("/", response_model=contactPydantic)
async def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    db_contact = Contact()
    db_contact.mail = contact.mail
    db_contact.nom = contact.nom
    db_contact.prenom = contact.prenom
    db_contact.telephone = contact.telephone
    db.add(db_contact)
    db.commit()
    db.refresh()
