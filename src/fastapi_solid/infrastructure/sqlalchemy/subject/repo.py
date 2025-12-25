from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_solid.application.interfaces.subjects.repo import SubjectRepository
from fastapi_solid.domain.subject.model import Subject
from fastapi_solid.infrastructure.sqlalchemy.subject.table import SubjectOrm
from fastapi_solid.infrastructure.sqlalchemy.setup.base_repo import AlchemyRepo
from fastapi_solid.utils.converters.alch_to_dc import to_dataclass


class AlchemySubjectRepo(SubjectRepository, AlchemyRepo[SubjectOrm]):
    model = SubjectOrm

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_by_id(self, id: UUID) -> Subject | None:
        orm = await self._get_by_id(id)
        return to_dataclass(orm, Subject) if orm else None

    async def create(self, subject: Subject) -> Subject:
        created = await self._create(subject.__dict__)
        return to_dataclass(created, Subject)
