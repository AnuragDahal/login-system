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
    existing_user = db.query(models.User).filter_by(
        username=request.username).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User already exists")

    user = models.User(username=request.username, password=request.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created successfully"}


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(
        username=request.username, password=request.password).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return {"message": "Login successful", "user_id": user.id, "username": user.username}
