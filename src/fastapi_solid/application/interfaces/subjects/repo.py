from abc import ABC, abstractmethod
from uuid import UUID
from fastapi_solid.domain.subject.model import Subject


class SubjectRepository(ABC):
    @abstractmethod
    async def get_by_id(self, id: UUID) -> Subject | None: ...

    @abstractmethod
    async def create(self, subject: Subject) -> Subject: ...

    @abstractmethod
    async def update(self, id: UUID, subject: Subject) -> Subject: ...

    @abstractmethod
    async def delete(self, id: UUID) -> None: ...
