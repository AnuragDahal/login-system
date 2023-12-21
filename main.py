from fastapi import FastAPI, APIRouter
from router import user
from core.database import engine
from core import models


app = FastAPI()
router = APIRouter()

models.Base.metadata.create_all(engine)


app.include_router(user.router)
