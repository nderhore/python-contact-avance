from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import api.api as api

app = FastAPI()


origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api.router, prefix="/api")
