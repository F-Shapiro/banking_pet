from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from enum import Enum


class AccountType(str, Enum):
    CHECKING = "CHECKING"
    SAVINGS = "SAVINGS"


class AccountStatus(str, Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    CLOSED = "CLOSED"


@dataclass
class Account:
    id: UUID
    client_id: UUID
    type: AccountType
    currency: str
    balance: int
    blocked_amount: int
    status: AccountStatus
    opened_at: datetime
    closed_at: datetime | None
