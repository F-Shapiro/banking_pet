from abc import ABC, abstractmethod
from uuid import UUID

from fastapi_solid.domain.account.model import Account


class AccountRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: UUID) -> Account | None: ...

    @abstractmethod
    async def get_by_client(self, client_id: UUID) -> list[Account]: ...

    @abstractmethod
    async def create(self, account: Account) -> Account: ...

    @abstractmethod
    async def update(self, id: UUID, account: Account) -> Account: ...
