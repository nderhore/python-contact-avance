from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

import api.api as api
from core.config.database import Base, engine

app = FastAPI()
templates = Jinja2Templates(directory="templates")

origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "contacts": [
                {
                    "nom": "Marushka",
                    "prenom": "Sergio",
                    "telephone": "3630",
                    "mail": "toto@jose.fr",
                },
                {"nom": "toto", "prenom": "titi", "telephone": "tutu", "mail": "tata"},
                {"nom": "de", "prenom": "de", "telephone": "d", "mail": "de"},
            ],
        },
    )


app.include_router(api.router, prefix="/api")
Base.metadata.create_all(bind=engine)
