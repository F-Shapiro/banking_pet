from fastapi_solid.application.interfaces.common.uow import UnitOfWork
from fastapi_solid.application.interfaces.transactions.repo import TransactionRepository
from fastapi_solid.application.transactions.dto import TransactionIn, TransactionOut


class TransactionService:
    def __init__(self, uow: UnitOfWork, repo: TransactionRepository):
        self.uow = uow
        self.repo = repo

    async def create(self, data: TransactionIn) -> TransactionOut:
        async with self.uow as uow:
            tx = await self.repo.create(data)
            await uow.commit()
        return TransactionOut.model_validate(tx, from_attributes=True)
