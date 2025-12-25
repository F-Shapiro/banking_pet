from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from fastapi_solid.domain.transaction.model import TransactionType, TransactionStatus


class TransactionIn(BaseModel):
    account_id: UUID
    type: TransactionType
    amount: float
    currency: str
    description: str | None = None


class TransactionUpdate(BaseModel):
    description: str | None = None
    status: TransactionStatus | None = None


class TransactionOut(TransactionIn):
    id: UUID
    status: TransactionStatus
    created_at: datetime
