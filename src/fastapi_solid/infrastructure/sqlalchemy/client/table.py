import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from fastapi_solid.infrastructure.sqlalchemy.setup.base_model import Base
from datetime import datetime
from fastapi_solid.domain.client.model import ClientStatus


class ClientOrm(Base):
    __tablename__ = "clients"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subject_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False)
    status: Mapped[ClientStatus] = mapped_column(Enum(ClientStatus), nullable=False, default=ClientStatus.ACTIVE)
    primary_account_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
