from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from enum import Enum


class ClientAccessRole(str, Enum):
    OWNER = "OWNER"
    USER = "USER"


@dataclass
class ClientAccess:
    id: UUID
    user_id: UUID
    client_id: UUID
    role: ClientAccessRole
    created_at: datetime
