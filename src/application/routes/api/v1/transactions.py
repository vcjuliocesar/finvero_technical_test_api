from fastapi import Depends,APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.infrastructure.middlewares.jwt_bearer import JWTBearer
from src.infrastructure.schemas.transaction_schema import TransactionSchema
from src.infrastructure.service.belvo.belvo import Belvo
from src.application.usecases.payment_transactions_use_case import PaymentTransactionsUseCase

transaction_router = APIRouter(prefix="/api/v1",tags=["Transactions"])

@transaction_router.get("/transactions",response_model=TransactionSchema, status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
async def get_transactions(use_case:PaymentTransactionsUseCase = Depends()):
    try:
        
        #use_case.execute()
        # transactions = await belvo.get_transactions()

        # transactions['results'] = [element for element in transactions['results']
        #            if element.get("category") == "Income & Payments"]
        
        # transactions['results'] = [
        #     {**item, 'account': item['account']['id']} for item in transactions['results']]

        # transactions['results'] = list(map(lambda x: {k: v for k, v in x.items(
        # ) if k not in ('merchant')}, transactions['results']))
        
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder({'results':use_case.execute()}))

    except Exception as error:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))