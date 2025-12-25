from abc import ABC, abstractmethod
from fastapi_solid.domain.transaction.model import Transaction
from fastapi_solid.application.transactions.dto import TransactionIn


class TransactionRepository(ABC):
    @abstractmethod
    async def create(self, data: TransactionIn) -> Transaction: ...

    @abstractmethod
    async def get_by_account(self, account_id) -> list[Transaction]: ...
