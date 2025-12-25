from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_solid.application.interfaces.cards.repo import CardRepository
from fastapi_solid.application.cards.dto import CardIn
from fastapi_solid.domain.card.model import Card
from fastapi_solid.infrastructure.sqlalchemy.card.table import CardOrm
from fastapi_solid.infrastructure.sqlalchemy.setup.base_repo import AlchemyRepo
from fastapi_solid.utils.converters.alch_to_dc import to_dataclass


class AlchemyCardRepo(CardRepository, AlchemyRepo[CardOrm]):
    model = CardOrm

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def create(self, data: CardIn) -> Card:
        card_orm = await self._create(data.model_dump())
        return to_dataclass(card_orm, Card)

    async def get_by_account(self, account_id: UUID) -> list[Card]:
        cards_orm = await self.get_by_account(account_id=account_id)
        return [to_dataclass(card, Card) for card in cards_orm]
