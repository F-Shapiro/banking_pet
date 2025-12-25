from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_solid.application.interfaces.auth_session.repo import AuthSessionRepository
from fastapi_solid.domain.auth_session.model import AuthSession
from fastapi_solid.infrastructure.sqlalchemy.auth_session.table import AuthSessionOrm
from fastapi_solid.infrastructure.sqlalchemy.setup.base_repo import AlchemyRepo
from fastapi_solid.utils.converters.alch_to_dc import to_dataclass


class AlchemyAuthSessionRepo(AuthSessionRepository, AlchemyRepo[AuthSessionOrm]):
    model = AuthSessionOrm

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_by_id(self, id: UUID) -> AuthSession | None:
        orm = await self._get_by_id(id)
        return to_dataclass(orm, AuthSession) if orm else None

    async def create(self, session: AuthSession) -> AuthSession:
        created = await self._create(session.__dict__)
        return to_dataclass(created, AuthSession)

    async def delete(self, id: UUID) -> None:
        await self._delete(id)
