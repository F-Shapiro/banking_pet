from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class UserIn(BaseModel):
    email: str
    phone: str | None
    password: str
    first_name: str
    last_name: str
    middle_name: str | None = None


class UserOut(UserIn):
    id: UUID
    created_at: datetime
    updated_at: datetime


class UserUpdate(BaseModel):
    phone: str | None
    first_name: str
    last_name: str
    middle_name: str | None = None
