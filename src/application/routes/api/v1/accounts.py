from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.infrastructure.schemas.account_schema import AccountSchema
from src.application.usecases.get_accounts_use_case import GetAccountsUseCase
from src.infrastructure.middlewares.jwt_bearer import JWTBearer
from src.infrastructure.service.belvo.belvo import Belvo


account_router = APIRouter(prefix="/api/v1",tags=["Accounts"])

@account_router.get("/accounts", response_model=AccountSchema,status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
async def get_accounts(use_case:GetAccountsUseCase = Depends()):
    try:

        # transactions = await belvo.get_transactions()
    
        # transactions['results'] = [element['account'] for element in transactions['results']]
        
        # transactions['results'] = list(map(lambda x: {k: v for k, v in x.items(
        # ) if k not in ('institution','balance','loan_data','credit_data')}, transactions['results']))
       
        
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(use_case.execute()))

    except Exception as error:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))