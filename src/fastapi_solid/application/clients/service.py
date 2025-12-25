from uuid import UUID

from fastapi_solid.application.exceptions.app_error import NotFound
from fastapi_solid.application.interfaces.clients.repo import ClientRepository
from fastapi_solid.application.interfaces.common.uow import UnitOfWork
from fastapi_solid.domain.client.model import Client


class ClientService:
    def __init__(self, uow: UnitOfWork, clients_repo: ClientRepository):
        self.uow = uow
        self.clients_repo = clients_repo

    async def get_by_id(self, client_id: UUID) -> Client:
        async with self.uow:
            client = await self.clients_repo.get_by_id(client_id)
            if not client:
                raise NotFound.domain_entity(Client, client_id)
            return client

    async def create(self, client: Client) -> Client:
        async with self.uow as uow:
            created = await self.clients_repo.create(client)
            await uow.commit()
            return created

    async def delete(self, client_id: UUID) -> None:
        async with self.uow as uow:
            await self.clients_repo.delete(client_id)
            await uow.commit()
