from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class AuthSessionIn(BaseModel):
    user_id: UUID
    client_id: UUID
    refresh_token_hash: str
    device_fingerprint: str
    expires_at: datetime


class AuthSessionOut(AuthSessionIn):
    id: UUID
    created_at: datetime
