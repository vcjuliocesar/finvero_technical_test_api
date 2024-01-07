from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.responses import JSONResponse
from src.service.belvo.belvo import Belvo

app = FastAPI()

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