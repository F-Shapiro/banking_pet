from sqlalchemy.orm import Mapped
from sqlalchemy import Enum

from fastapi_solid.infrastructure.sqlalchemy.setup.base_model import Base
from fastapi_solid.domain.client.model import ClientStatus


class ClientOrm(Base):
    __tablename__ = "clients"

    subject_id: Mapped[str]
    status: Mapped[ClientStatus] = Enum(ClientStatus)
    primary_account_id: Mapped[str | None]
