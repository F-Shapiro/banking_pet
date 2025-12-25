import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from fastapi_solid.infrastructure.sqlalchemy.setup.base_model import Base
from uuid import uuid4
from datetime import datetime
from fastapi_solid.domain.client_access.model import ClientAccessRole


class ClientAccessOrm(Base):
    __tablename__ = "client_access"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    client_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    role: Mapped[ClientAccessRole] = mapped_column(Enum(ClientAccessRole), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
