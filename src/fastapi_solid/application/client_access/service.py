from uuid import UUID
from fastapi_solid.application.interfaces.client_access.repo import ClientAccessRepository
from fastapi_solid.application.interfaces.common.uow import UnitOfWork
from fastapi_solid.domain.client_access.model import ClientAccess
from fastapi_solid.application.exceptions.app_error import NotFound


class ClientAccessService:
    def __init__(self, uow: UnitOfWork, repo: ClientAccessRepository):
        self.uow = uow
        self.repo = repo

    async def create(self, access: ClientAccess) -> ClientAccess:
        async with self.uow as uow:
            created = await self.repo.create(access)
            await uow.commit()
            return created

    async def get_by_id(self, id: UUID) -> ClientAccess:
        async with self.uow:
            entity = await self.repo.get_by_id(id)
            if not entity:
                raise NotFound.domain_entity(ClientAccess, id)
            return entity
