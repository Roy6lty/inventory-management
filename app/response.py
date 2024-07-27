from pydantic import field_validator, UUID4
from app.base import AbstractBaseModel


class UserResponse(AbstractBaseModel):
    id: UUID4
    name: str
    age: int
    address: str
