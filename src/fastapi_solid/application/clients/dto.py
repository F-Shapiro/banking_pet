from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from enum import Enum


class ClientStatus(str, Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    CLOSED = "CLOSED"


class ClientIn(BaseModel):
    subject_id: UUID
    status: ClientStatus = ClientStatus.ACTIVE
    primary_account_id: UUID | None = None


class ClientOut(ClientIn):
    id: UUID
    created_at: datetime
    updated_at: datetime


class ClientUpdate(BaseModel):
    status: ClientStatus | None = None
    primary_account_id: UUID | None = None
