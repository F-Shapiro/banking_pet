from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from enum import Enum


class SubjectType(str, Enum):
    PERSON = "PERSON"
    COMPANY = "COMPANY"


class SubjectIn(BaseModel):
    type: SubjectType
    name: str
    tax_id: str | None = None
    registration_number: str | None = None


class SubjectOut(SubjectIn):
    id: UUID
    created_at: datetime


class SubjectUpdate(BaseModel):
    name: str | None = None
    tax_id: str | None = None
    registration_number: str | None = None
