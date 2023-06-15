from fastapi import APIRouter

from api.endpoint.contact_api import router as router_contact
from api.endpoint.login_api import router as router_login


router = APIRouter()

router.include_router(
    router_contact,
    prefix="/contact",
    responses={404: {"description": "not found"}},
)

router.include_router(
    router_login,
    prefix="/login",
    responses={404: {"description": "not found"}},
)
