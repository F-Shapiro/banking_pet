from uuid import UUID

from fastapi_solid.application.interfaces.subjects.repo import SubjectRepository
from fastapi_solid.application.interfaces.common.uow import UnitOfWork
from fastapi_solid.domain.subject.model import Subject
from fastapi_solid.application.exceptions.app_error import NotFound


class SubjectService:
    def __init__(self, uow: UnitOfWork, repo: SubjectRepository):
        self.uow = uow
        self.repo = repo

    async def get_by_id(self, id: UUID) -> Subject:
        async with self.uow:
            entity = await self.repo.get_by_id(id)
            if not entity:
                raise NotFound.domain_entity(Subject, id)
            return entity

    async def create(self, subject: Subject) -> Subject:
        async with self.uow as uow:
            created = await self.repo.create(subject)
            await uow.commit()
            return created
