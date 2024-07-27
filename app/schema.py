from pydantic import field_validator
from app.base import AbstractBaseModel


class UserSchema(AbstractBaseModel):
    name: str
    age: int
    address: str
