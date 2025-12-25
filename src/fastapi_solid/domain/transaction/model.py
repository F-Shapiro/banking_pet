from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from enum import Enum
from decimal import Decimal


class TransactionType(str, Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"


class TransactionStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


@dataclass
class Transaction:
    id: UUID
    account_id: UUID
    type: TransactionType
    amount: Decimal
    currency: str
    description: str | None
    status: TransactionStatus
    created_at: datetime
