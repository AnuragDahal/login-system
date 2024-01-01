from pydantic import BaseModel


class Signup(BaseModel):
    Name: str
    Email: str
    password: str


class Login(BaseModel):
    Email: str
    password: str


class view(BaseModel):
    Email: str
    password: str

    class Config():
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
