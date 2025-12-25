from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_solid.application.interfaces.clients.repo import ClientRepository
from fastapi_solid.domain.client.model import Client
from fastapi_solid.infrastructure.sqlalchemy.client.table import ClientOrm
from fastapi_solid.infrastructure.sqlalchemy.setup.base_repo import AlchemyRepo
from fastapi_solid.utils.converters.alch_to_dc import to_dataclass


class AlchemyClientRepo(ClientRepository, AlchemyRepo[ClientOrm]):
    model = ClientOrm

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_by_id(self, id: UUID) -> Client | None:
        orm = await self._get_by_id(id)
        return to_dataclass(orm, Client) if orm else None

    async def get_all(self, pagination=None) -> list[Client]:
        orms = await self._get_all(pagination)
        return [to_dataclass(o, Client) for o in orms]

    async def create(self, client: Client) -> Client:
        created = await self._create(client.__dict__)
        return to_dataclass(created, Client)

    async def update(self, id: UUID, client: Client) -> Client:
        updated = await self._update_by_id(id, client.__dict__)
        return to_dataclass(updated, Client)

    async def delete(self, id: UUID) -> None:
        await self._delete(id)
