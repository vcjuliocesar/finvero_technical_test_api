from fastapi import Depends,APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.infrastructure.schemas.transaction_schema import TransactionSchema
from src.infrastructure.service.belvo.belvo import Belvo

transaction_router = APIRouter(prefix="/api/v1",tags=["Transactions"])

@transaction_router.get("/transactions",response_model=TransactionSchema, status_code=status.HTTP_200_OK)
async def get_transactions(belvo: Belvo = Depends()):
    try:
        
        transactions = await belvo.get_transactions()

        transactions['results'] = [element for element in transactions['results']
                   if element.get("category") == "Income & Payments"]
        
        transactions['results'] = [
            {**item, 'account': item['account']['id']} for item in transactions['results']]

        transactions['results'] = list(map(lambda x: {k: v for k, v in x.items(
        ) if k not in ('merchant')}, transactions['results']))
        
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder( transactions['results']))

    except Exception as error:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))