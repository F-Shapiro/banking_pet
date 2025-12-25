from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from enum import Enum


class ClientStatus(str, Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    CLOSED = "CLOSED"


@dataclass
class Client:
    id: UUID
    subject_id: UUID
    status: ClientStatus
    primary_account_id: UUID | None
    created_at: datetime
    updated_at: datetime
