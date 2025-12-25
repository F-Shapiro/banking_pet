from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class CardIn(BaseModel):
    account_id: UUID
    last4: str
    brand: str


class CardOut(CardIn):
    id: UUID
    created_at: datetime


class CardUpdate(BaseModel):
    pass
