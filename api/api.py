from fastapi import APIRouter
from api.endpoint.contact_api import router as router_contact

router = APIRouter()

router.include_router(router_contact, prefix="/contact",
                      responses={404: {"description":"not found"}},)

