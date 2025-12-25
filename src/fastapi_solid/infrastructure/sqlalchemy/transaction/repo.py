from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_solid.application.interfaces.transactions.repo import TransactionRepository
from fastapi_solid.application.transactions.dto import (
    TransactionIn,
    TransactionUpdate,
)
from fastapi_solid.domain.transaction.model import Transaction
from fastapi_solid.infrastructure.sqlalchemy.transaction.table import TransactionOrm
from fastapi_solid.infrastructure.sqlalchemy.setup.base_repo import AlchemyRepo
from fastapi_solid.utils.converters.alch_to_dc import to_dataclass


class AlchemyTransactionRepo(
    TransactionRepository,
    AlchemyRepo[TransactionOrm],
):
    model = TransactionOrm

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_by_id(self, id: UUID) -> Transaction | None:
        tx_orm = await self._get_by_id(id)
        return to_dataclass(tx_orm, Transaction) if tx_orm else None

    async def get_by_account(self, account_id: UUID) -> list[Transaction]:
        txs_orm = await self.get_by_account(account_id=account_id)
        return [to_dataclass(tx, Transaction) for tx in txs_orm]

    async def create(self, data: TransactionIn) -> Transaction:
        tx_orm = await self._create(data.model_dump())
        return to_dataclass(tx_orm, Transaction)

    async def update(
        self,
        id: UUID,
        update_data: TransactionUpdate,
    ) -> Transaction:
        tx_orm = await self._update_by_id(id, update_data.model_dump())
        return to_dataclass(tx_orm, Transaction)

    async def delete(self, id: UUID) -> None:
        await self._delete(id)
