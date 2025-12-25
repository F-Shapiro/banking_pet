from sqlalchemy.orm import Mapped
from sqlalchemy import Numeric, String, ForeignKey
from fastapi_solid.infrastructure.sqlalchemy.setup.base_model import Base


class TransactionOrm(Base):
    __tablename__ = "transactions"

    account_id: Mapped[str] = ForeignKey("accounts.id")
    amount: Mapped[Numeric]
    type: Mapped[String]
    description: Mapped[String | None]
