from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse
from datetime import datetime
from core.config.security import verify_password
from core.models.user import User
from core.schema.userSchema import UserBase
from core.service.userService import get_user, create_token, current_active_user

router = APIRouter()


@router.post("/", response_class=JSONResponse)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    mon_User: User = await get_user(form_data.username)
    if mon_User is not None:
        if verify_password(
                plain_password=form_data.password, password_hash=mon_User.password
        ):
            access_token = create_token(data={"sub": form_data.username, "iat": datetime.now().timestamp()})
            return JSONResponse(
                content={"access_token": access_token,
                         "token_type": "BEARER"}
            )
        else:
            return JSONResponse(
                content={"message": "mot de passe faux"}, status_code=401
            )
    else:
        return JSONResponse(content={"message": "user inexistant"}, status_code=404)

@router.get("/me",response_model=UserBase)
async def userData(current_User=Annotated[User,Depends(current_active_user)]):
    return current_User
