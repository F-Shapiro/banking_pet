from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from enum import Enum


class SubjectType(str, Enum):
    PERSON = "PERSON"
    COMPANY = "COMPANY"


@dataclass
class Subject:
    id: UUID
    type: SubjectType
    name: str
    tax_id: str | None
    registration_number: str | None
    created_at: datetime
