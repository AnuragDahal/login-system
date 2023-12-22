from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from core import models, schemas, database
from typing import List

get_db = database.get_db
router = APIRouter(
    prefix="/user",
    tags=["Authentication"]
)


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(request: schemas.Signup, db: Session = Depends(get_db)):
    user = models.User(username=request.username, password=request.password)
    if not user:
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, detail={
                            "Credentials already exists try new one"})
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username ==
                                        request.username, models.User.password == request.password).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    return "Login Successful"
