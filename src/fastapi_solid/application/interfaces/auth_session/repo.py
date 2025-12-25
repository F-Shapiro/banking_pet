from abc import ABC, abstractmethod
from uuid import UUID
from fastapi_solid.domain.auth_session.model import AuthSession


class AuthSessionRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: UUID) -> AuthSession | None: ...

    @abstractmethod
    async def create(self, session: AuthSession) -> AuthSession: ...

    @abstractmethod
    async def delete(self, id: UUID) -> None: ...
