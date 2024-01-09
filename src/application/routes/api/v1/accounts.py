from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from src.infrastructure.service.belvo.belvo import Belvo


account_router = APIRouter(prefix="/api/v1",tags=["Accounts"])

@account_router.get("/accounts", status_code=status.HTTP_200_OK)
async def get_accounts(belvo: Belvo = Depends()):
    try:

        transactions = await belvo.get_transactions()
    
        transactions['results'] = [element['account'] for element in transactions['results']]
        
        transactions['results'] = list(map(lambda x: {k: v for k, v in x.items(
        ) if k not in ('institution','balance','loan_data','credit_data')}, transactions['results']))
       
        
        return JSONResponse(status_code=status.HTTP_200_OK, content=transactions['results'] )

    except Exception as error:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))