from sqlalchemy.orm import Mapped
from sqlalchemy import String, ForeignKey

from fastapi_solid.infrastructure.sqlalchemy.setup.base_model import Base


class CardOrm(Base):
    __tablename__ = "cards"

    account_id: Mapped[str] = ForeignKey("accounts.id", ondelete="CASCADE")
    last4: Mapped[str] = String(4)
    brand: Mapped[str] = String(32)
