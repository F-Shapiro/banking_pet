import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, ForeignKey, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from fastapi_solid.infrastructure.sqlalchemy.setup.base_model import Base
from datetime import datetime
from fastapi_solid.domain.card.model import CardType, CardStatus


class CardOrm(Base):
    __tablename__ = "cards"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    account_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False)
    type: Mapped[CardType] = mapped_column(Enum(CardType), nullable=False)
    masked_number: Mapped[str] = mapped_column(String(16), nullable=False)
    expiration_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[CardStatus] = mapped_column(Enum(CardStatus), nullable=False, default=CardStatus.ACTIVE)
    issued_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
