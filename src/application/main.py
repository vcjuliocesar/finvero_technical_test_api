from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.application.usecases.get_accounts_use_case import GetAccountsUseCase
from src.application.usecases.get_transactions_use_case import GetTransactionsUseCase
from src.domain.models.account_entity import AccountEntity
from src.domain.models.base_entity import init
from src.infrastructure.schemas.transaction_schema import TransactionSchema
from src.infrastructure.service.belvo.belvo import Belvo
from src.domain.models.transaction_entity import TransactionEntity
from src.application.routes.api.v1.transactions import transaction_router
from src.application.routes.api.v1.accounts import account_router 
from src.application.routes.api.v1.amounts_by_category import amounts_by_category_router
from src.application.routes.api.v1.income_and_expense_analysis import income_and_expense_analysis_router
from src.application.routes.api.v1.balance import balance_router

app = FastAPI()


async def startup_event():
    pass
    #instance = Belvo()

    # transactions = await instance.post_retrieve_transactions()

    # accounts = await instance.post_retrieve_accounts()

    # if transactions == 201 and accounts == 201:

    # transaction_list = await instance.get_transactions()

    # account_list = await instance.get_accounts()

    # insert_account_data(account_list)
    # insert_transactions_data(transaction_list)
    #


async def shutdown_event():
    print("shut down app...")

app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)



app.include_router(transaction_router)

app.include_router(account_router)

app.include_router(amounts_by_category_router)

app.include_router(income_and_expense_analysis_router)

app.include_router(balance_router)



init()
