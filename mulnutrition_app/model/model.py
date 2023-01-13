from pydantic import BaseModel


class Mul(BaseModel):
    name: str
    email: str
    password: str
