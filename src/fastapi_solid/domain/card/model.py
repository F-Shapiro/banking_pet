from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from enum import Enum


class CardType(str, Enum):
    PHYSICAL = "PHYSICAL"
    VIRTUAL = "VIRTUAL"


class CardStatus(str, Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    EXPIRED = "EXPIRED"


@dataclass
class Card:
    id: UUID
    account_id: UUID
    type: CardType
    masked_number: str
    expiration_date: datetime
    status: CardStatus
    issued_at: datetime
