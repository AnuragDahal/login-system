from pydantic import BaseModel


class Signup(BaseModel):
    username: str
    password: str


class Login(BaseModel):
    username: str
    password: str


class view(BaseModel):
    username: str
    password: str

    class Config():
        from_attributes = True
