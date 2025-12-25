from dataclasses import dataclass
from uuid import UUID
from datetime import date, datetime


@dataclass(frozen=True)
class User:
    id: UUID
    email: str
    phone: str
    password_hash: str

    first_name: str
    last_name: str
    middle_name: str | None

    birth_date: date

    passport_number: str
    passport_issued_by: str
    passport_issued_at: date

    INN: str
    SNILS: str

    is_active: bool
    mfa_enabled: bool

    created_at: datetime
    updated_at: datetime
