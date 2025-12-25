from uuid import UUID

from fastapi_solid.application.interfaces.cards.repo import CardRepository
from fastapi_solid.application.interfaces.common.uow import UnitOfWork
from fastapi_solid.application.cards.dto import CardIn, CardOut
from fastapi_solid.domain.card.model import Card
from fastapi_solid.application.exceptions.app_error import NotFound


class CardService:
    def __init__(self, uow: UnitOfWork, repo: CardRepository):
        self.uow = uow
        self.repo = repo

    async def create(self, card_in: CardIn) -> CardOut:
        async with self.uow as uow:
            card = await self.repo.create(card_in)
            await uow.commit()
        return CardOut.model_validate(card, from_attributes=True)

    async def get_by_account(self, account_id: UUID) -> list[CardOut]:
        async with self.uow:
            cards = await self.repo.get_by_account(account_id)
            if not cards:
                raise NotFound.domain_entity(Card, account_id)
            return [CardOut.model_validate(c, from_attributes=True) for c in cards]
