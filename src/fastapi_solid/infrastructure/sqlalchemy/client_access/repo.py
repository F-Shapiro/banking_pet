from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_solid.application.interfaces.client_access.repo import ClientAccessRepository
from fastapi_solid.domain.client_access.model import ClientAccess
from fastapi_solid.infrastructure.sqlalchemy.client_access.table import ClientAccessOrm
from fastapi_solid.infrastructure.sqlalchemy.setup.base_repo import AlchemyRepo
from fastapi_solid.utils.converters.alch_to_dc import to_dataclass


class AlchemyClientAccessRepo(ClientAccessRepository, AlchemyRepo[ClientAccessOrm]):
    model = ClientAccessOrm

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_by_id(self, id: UUID) -> ClientAccess | None:
        orm = await self._get_by_id(id)
        return to_dataclass(orm, ClientAccess) if orm else None

    async def create(self, access: ClientAccess) -> ClientAccess:
        created = await self._create(access.__dict__)
        return to_dataclass(created, ClientAccess)

    async def delete(self, id: UUID) -> None:
        await self._delete(id)
