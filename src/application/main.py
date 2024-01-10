import time
from fastapi import FastAPI
from src.infrastructure.service.belvo.belvo import Belvo
from src.domain.models.base_entity import init
from src.domain.models.account_entity import AccountEntity
from src.domain.models.transaction_entity import TransactionEntity
from src.presentation.data.extract_data import extract_data_on_startup
from src.infrastructure.exceptions.http_exception import get_http_exception
from src.infrastructure.exceptions.errorhandler import ErrorHandler
from src.application.routes.api.v1.transactions import transaction_router
from src.application.routes.api.v1.accounts import account_router 
from src.application.routes.api.v1.amounts_by_category import amounts_by_category_router
from src.application.routes.api.v1.income_and_expense_analysis import income_and_expense_analysis_router
from src.application.routes.api.v1.balance import balance_router
from src.application.routes.api.v1.auth import auth_router
from src.application.routes.api.v1.user import user_router


app = FastAPI()


async def startup_event():
    
    instance = Belvo()
    
    max_retries = 3
    
    retries = 0
     
    while retries < max_retries:
        
        try:
            
            account_list = await instance.get_accounts()
            transactions = await instance.get_transactions()
            
            if account_list.status_code == 200 > 0 and transactions == 200:
                
                extract_data_on_startup({'accounts':account_list.json(),'transactions':transactions.json()})
                
                break
            
        except Exception as error:
            
            raise get_http_exception(error)
        
        retries +=1
    
        time.sleep(1)

async def shutdown_event():
    print("shut down app...")

app.add_event_handler("startup", startup_event)

app.add_event_handler("shutdown", shutdown_event)

app.add_middleware(ErrorHandler)

app.include_router(auth_router)

app.include_router(user_router)

app.include_router(transaction_router)

app.include_router(account_router)

app.include_router(amounts_by_category_router)

app.include_router(income_and_expense_analysis_router)

app.include_router(balance_router)




init()
