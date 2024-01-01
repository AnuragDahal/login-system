from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from core import models, schemas, database
from . import hash

get_db = database.get_db


router = APIRouter(
    tags=["Authentication"]
)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(request: schemas.Login, db: Session = Depends(get_db)):

    user = db.query(models.User).filter_by(Email=request.Email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
# This is checking if the result of the check_pw method is False. If it is, it means the passwords didn't match,
    if not hash.Encryption.check_pw(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    return {"message": "Login successful", "user_id": user.id, "Name": user.Name}
