from pydantic import BaseModel


class Signup(BaseModel):
    Name: str
    Email: str
    password: str
    time: int


class Login(BaseModel):
    Email: str
    password: str


class view(BaseModel):
    Email: str
    password: str

    class Config():
        from_attributes = True
