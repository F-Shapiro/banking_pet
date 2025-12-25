from abc import ABC, abstractmethod
from uuid import UUID

from fastapi_solid.application.interfaces.common.pagination import Pagination
from fastapi_solid.domain.client.model import Client


class ClientRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: UUID) -> Client | None: ...

    @abstractmethod
    async def get_all(self, pagination: Pagination | None = None) -> list[Client]: ...

    @abstractmethod
    async def create(self, client: Client) -> Client: ...

    @abstractmethod
    async def update(self, id: UUID, client: Client) -> Client: ...

    @abstractmethod
    async def delete(self, id: UUID) -> None: ...
