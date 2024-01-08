from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.responses import JSONResponse
from src.domain.models.base_entity import init
from src.service.belvo.belvo import Belvo

app = FastAPI()

async def startup_event():
    instance = Belvo()
    transactions = await instance.post_retrieve_transactions()
    accounts = await instance.post_retrieve_accounts()
    print("transactions",transactions)
    print("accounts",accounts)

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
    
    
