from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from core.config.database import get_db
from core.models.contact import Contact
from core.schema.ContactSchema import ContactCreate, ContactUpdate
from core.schema.ContactSchema import Contact as contactPydantic

router = APIRouter()


@router.post("/")
async def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    db_contact = Contact()
    db_contact.mail = contact.mail
    db_contact.nom = contact.nom
    db_contact.prenom = contact.prenom
    db_contact.telephone = contact.telephone
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return JSONResponse(content={"message": "Intégré"})

@router.get("/{id}",response_model=contactPydantic)
async def get_contact_by_id(contact_id: int, db: Session = Depends(get_db)) -> contactPydantic:
   return db.query(Contact).filter(Contact.id == contact_id).first()

@router.get("/", response_model=list[contactPydantic])
async def get_contacts(db: Session = Depends(get_db)):
    return db.query(Contact).all()

@router.put("/{contact_id}",response_class=JSONResponse)
async def update_contact_by_id(contact_id : int, contact: ContactUpdate, db : Session = Depends(get_db)):
    old_contact = get_contact_by_id(contact_id)
    if old_contact:
        old_contact.nom = contact.nom
        old_contact.mail = contact.mail
        old_contact.telephone = contact.telephone
        old_contact.prenom = contact.prenom
        db.commit()
        db.refresh(old_contact)
        return JSONResponse(content={"message": "Contact mis à jour avec succès", "contacts" : old_contact})
    return JSONResponse(content={"message":"Contact non trouvé."})

