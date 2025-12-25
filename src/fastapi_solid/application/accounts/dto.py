from datetime import datetime
from uuid import UUID
from decimal import Decimal
from pydantic import BaseModel


class AccountIn(BaseModel):
    user_id: UUID
    is_main: bool = False


class AccountOut(AccountIn):
    id: UUID
    balance: Decimal
    created_at: datetime


class AccountUpdate(BaseModel):
    is_main: bool | None = None
