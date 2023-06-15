from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse
from datetime import datetime
from core.config.security import verify_password
from core.models.user import User
from core.service.userService import get_user, create_token

router = APIRouter()


@router.post('/', response_model=JSONResponse)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    mon_User: User = get_user(form_data.username)
    if mon_User is not None:
        if verify_password(plain_password=form_data.password,
                           password_hash=mon_User.password):

            create_token(data={"sub": form_data.username,
                               "iat": datetime.now()})

        else:
            return JSONResponse(content={"message": "mot de passe faux"},
                                status_code=401)
    else:
        return JSONResponse(content={"message": "non trouvé"},
                            status_code=404)
