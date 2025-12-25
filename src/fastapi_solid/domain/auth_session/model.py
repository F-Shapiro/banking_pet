from dataclasses import dataclass
from uuid import UUID
from datetime import datetime


@dataclass
class AuthSession:
    id: UUID
    user_id: UUID
    client_id: UUID
    refresh_token_hash: str
    device_fingerprint: str
    expires_at: datetime
    created_at: datetime
