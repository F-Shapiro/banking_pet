from uuid import UUID
from fastapi_solid.application.interfaces.auth_session.repo import AuthSessionRepository
from fastapi_solid.application.interfaces.common.uow import UnitOfWork
from fastapi_solid.domain.auth_session.model import AuthSession
from fastapi_solid.application.exceptions.app_error import NotFound


class AuthSessionService:
    def __init__(self, uow: UnitOfWork, repo: AuthSessionRepository):
        self.uow = uow
        self.repo = repo

    async def create(self, session: AuthSession) -> AuthSession:
        async with self.uow as uow:
            created = await self.repo.create(session)
            await uow.commit()
            return created

    async def get_by_id(self, id: UUID) -> AuthSession:
        async with self.uow:
            entity = await self.repo.get_by_id(id)
            if not entity:
                raise NotFound.domain_entity(AuthSession, id)
            return entity
