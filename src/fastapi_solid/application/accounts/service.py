from uuid import UUID

from fastapi_solid.application.exceptions.app_error import NotFound
from fastapi_solid.application.interfaces.accounts.repo import AccountRepository
from fastapi_solid.application.interfaces.common.uow import UnitOfWork
from fastapi_solid.domain.account.model import Account


class AccountService:
    def __init__(self, uow: UnitOfWork, accounts_repo: AccountRepository):
        self.uow = uow
        self.accounts_repo = accounts_repo

    async def get_by_id(self, account_id: UUID) -> Account:
        async with self.uow:
            account = await self.accounts_repo.get_by_id(account_id)
            if not account:
                raise NotFound.domain_entity(Account, account_id)
            return account

    async def get_by_client(self, client_id: UUID) -> list[Account]:
        async with self.uow:
            return await self.accounts_repo.get_by_client(client_id)
