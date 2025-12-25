from abc import ABC, abstractmethod
from uuid import UUID
from fastapi_solid.domain.client_access.model import ClientAccess


class ClientAccessRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: UUID) -> ClientAccess | None: ...

    @abstractmethod
    async def create(self, access: ClientAccess) -> ClientAccess: ...

    @abstractmethod
    async def delete(self, id: UUID) -> None: ...
