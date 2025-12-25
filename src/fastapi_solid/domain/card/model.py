from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Card:
    id: UUID
    account_id: UUID
    last4: str
    brand: str
    created_at: datetime
