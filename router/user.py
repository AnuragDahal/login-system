from fastapi import APIRouter, Depends, status, HTTPException, Request
from sqlalchemy.orm import Session
from core import models, schemas, database
from . import hash, realtime, oauth
from .jwt_token import check_cookie

get_db = database.get_db
router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(request: schemas.Signup, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter_by(
        Name=request.Name, Email=request.Email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User already exists")

    user = models.User(Name=request.Name, Email=request.Email,
                       password=hash.Encryption.bcrypt(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    time_now = realtime.time.current_time()
    print(time_now)
    return {"message": "User created successfully",
            "time": f"{time_now}"}


@router.get("/about", status_code=status.HTTP_200_OK)
async def about(current_user: schemas.Signup = Depends(oauth.get_current_user)):
    return {"name": "Anurag",
            "age": "20",
            "college": "TU"}


@router.post("/about/{name}/{address}/{age}")
async def put_details(name: str, address: str, age: int):
    return {"Name": f"{name}",
            "Address": f"{address}",
            "Age": f"{age}"}


@router.get("/cookie-login/check", status_code=status.HTTP_200_OK)
async def cookie_login(req: Request, dependencies: Session = Depends(check_cookie)):
    if dependencies:
        return {"detail": "Cookie auhtenticated successfully"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Cookie not authenticated")
