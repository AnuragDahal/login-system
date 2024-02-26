from fastapi import APIRouter, Depends, status, HTTPException,Response,Request
from sqlalchemy.orm import Session
from core import models, database
from . import hash, jwt_token
from datetime import timedelta
from .jwt_token import verify_token
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordRequestForm
import os

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.environ.get("Access_Token_Expire_Minutes"))


get_db = database.get_db


router = APIRouter(
    tags=["Authentication"]
)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(req:Request,res:Response, request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(models.User).filter_by(Email=request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
# This is checking if the result of the check_pw method is False. If it is, it means the passwords didn't match,
    if not hash.Encryption.check_pw(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

# GENERATE A JWT TOKEN AND set it  as cookie in the  response 
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt_token.create_access_token(
        data={"sub": user.Email}, expires_delta=access_token_expires)
    
    res.set_cookie(key="login-token", value=access_token)        
    return {"token": access_token, "token_type": "bearer"}
    
    
@router.post("/logout", status_code=status.HTTP_200_OK)
async def logout(res:Response, dep:Depends(verify_token)):
    try:
        res.delete_cookie(key="login-token")
        return {"detail":"Logged out successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))