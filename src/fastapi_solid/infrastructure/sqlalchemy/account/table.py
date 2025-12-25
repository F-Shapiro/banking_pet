from sqlalchemy.orm import Mapped
from sqlalchemy import Enum

from fastapi_solid.infrastructure.sqlalchemy.setup.base_model import Base
from fastapi_solid.domain.account.model import AccountType, AccountStatus


class AccountOrm(Base):
    __tablename__ = "accounts"

    client_id: Mapped[str]
    type: Mapped[AccountType] = Enum(AccountType)
    currency: Mapped[str]
    balance: Mapped[int]
    blocked_amount: Mapped[int]
    status: Mapped[AccountStatus] = Enum(AccountStatus)
