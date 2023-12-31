from fastapi import FastAPI
from router import user, auth
from core.database import engine
from core import models
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://www.nepalieducate.com",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5500"


]

app = FastAPI(
    title="Login-Api"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(engine)


app.include_router(auth.router)
app.include_router(user.router)
