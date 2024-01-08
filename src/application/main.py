from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.responses import JSONResponse
from src.domain.models.institution_entity import InstitutionEntity
from src.domain.models.account_entity import AccountEntity
from src.domain.models.balance_entity import BalanceEntity
from src.domain.models.credit_data_entity import CreditDataEntity
from src.domain.models.loan_data_entity import LoanDataEntity
from src.domain.models.merchant_entity import MerchantEntity
from src.domain.models.transaction_entity import TransactionEntity
from src.domain.models.base_entity import init
from src.infrastructure.service.belvo.belvo import Belvo

app = FastAPI()

async def startup_event():
    
    instance = Belvo()
    
    transactions = await instance.post_retrieve_transactions()
    
    accounts = await instance.post_retrieve_accounts()
    
    if transactions == 201 and accounts == 201:
        
        transaction_list = await instance.get_transactions()
        
        account_list = await instance.get_accounts()
        

async def shutdown_event():
    print("shut down app...")

app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)     

@app.get("/transactions", status_code=status.HTTP_200_OK)
async def get_transactions(belvo: Belvo = Depends()):
    try:
        
        transactions = await belvo.get_transactions()
        
        print(transactions)

        return JSONResponse(status_code=status.HTTP_200_OK, content=transactions['results'])

    except Exception as error:

        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
    
@app.get("/accounts", status_code=status.HTTP_200_OK)
async def get_transactions(belvo: Belvo = Depends()):
    try:
        
        accounts = await belvo.get_accounts()
        
        return JSONResponse(status_code=status.HTTP_200_OK, content=accounts['results'])

    except Exception as error:

        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
    
    
init()