from datetime import datetime
from uuid import UUID
from pydantic import BaseModel
from enum import Enum


class ClientAccessRole(str, Enum):
    OWNER = "OWNER"
    USER = "USER"


class ClientAccessIn(BaseModel):
    user_id: UUID
    client_id: UUID
    role: ClientAccessRole


class ClientAccessOut(ClientAccessIn):
    id: UUID
    created_at: datetime


class ClientAccessUpdate(BaseModel):
    role: ClientAccessRole | None = None
