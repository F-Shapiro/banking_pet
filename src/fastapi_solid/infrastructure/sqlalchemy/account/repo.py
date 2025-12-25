from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_solid.application.interfaces.accounts.repo import AccountRepository
from fastapi_solid.domain.account.model import Account
from fastapi_solid.infrastructure.sqlalchemy.account.table import AccountOrm
from fastapi_solid.infrastructure.sqlalchemy.setup.base_repo import AlchemyRepo
from fastapi_solid.utils.converters.alch_to_dc import to_dataclass


class AlchemyAccountRepo(AccountRepository, AlchemyRepo[AccountOrm]):
    model = AccountOrm

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_by_id(self, id: UUID) -> Account | None:
        orm = await self._get_by_id(id)
        return to_dataclass(orm, Account) if orm else None

    async def get_by_client(self, client_id: UUID) -> list[Account]:
        orms = await self._filter_by(client_id=client_id)
        return [to_dataclass(o, Account) for o in orms]

    async def create(self, account: Account) -> Account:
        created = await self._create(account.__dict__)
        return to_dataclass(created, Account)
