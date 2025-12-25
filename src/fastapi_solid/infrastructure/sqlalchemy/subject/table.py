import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from fastapi_solid.infrastructure.sqlalchemy.setup.base_model import Base
from datetime import datetime
from fastapi_solid.domain.subject.model import SubjectType


class SubjectOrm(Base):
    __tablename__ = "subjects"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type: Mapped[SubjectType] = mapped_column(Enum(SubjectType), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    tax_id: Mapped[str | None] = mapped_column(String(32), nullable=True)
    registration_number: Mapped[str | None] = mapped_column(String(32), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
