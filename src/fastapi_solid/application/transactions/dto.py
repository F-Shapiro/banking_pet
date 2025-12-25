from datetime import datetime
from uuid import UUID
from decimal import Decimal
from pydantic import BaseModel


class TransactionIn(BaseModel):
    account_id: UUID
    amount: Decimal
    type: str
    description: str | None = None


class TransactionOut(TransactionIn):
    id: UUID
    created_at: datetime
