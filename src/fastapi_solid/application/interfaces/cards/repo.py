from abc import ABC, abstractmethod
from uuid import UUID
from fastapi_solid.domain.card.model import Card
from fastapi_solid.application.cards.dto import CardIn


class CardRepository(ABC):
    @abstractmethod
    async def create(self, data: CardIn) -> Card: ...

    @abstractmethod
    async def get_by_account(self, account_id: UUID) -> list[Card]: ...
