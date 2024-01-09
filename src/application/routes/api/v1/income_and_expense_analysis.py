import re
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder 
from src.infrastructure.exceptions.invalid_account_id_exception import InvalidAccountIdException
from src.infrastructure.middlewares.jwt_bearer import JWTBearer
from src.infrastructure.service.belvo.belvo import Belvo

income_and_expense_analysis_router = APIRouter(prefix="/api/v1",tags=["Analysis"])

@income_and_expense_analysis_router.get("/income_and_expense_analysis", status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
async def get_income_and_expense_analysis(account_id:str,belvo: Belvo = Depends()):
    try:
        #user_id ="9cf598dc-3b6c-43e6-9c72-94b305d7837c"
        
        regex_pattern = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
        
        is_valid = bool(re.match(regex_pattern, account_id))
        
        if not is_valid:
            
            raise InvalidAccountIdException()
        
        transactions = await belvo.get_transactions()
        
        transactions['results'] = [
            {**item, 'account': item['account']['id']} for item in transactions['results']]
        
        transactions['results'] = list(map(lambda x: {k: v for k, v in x.items(
        ) if k not in ('merchant')}, transactions['results']))
        
        transactions['results'] = [element for element in transactions['results']
                   if element.get("account") == account_id]
        
        inflow = [elements for elements in transactions['results'] if elements['type'] == "INFLOW" and elements['status'] == 'PROCESSED']
        outlow = [elements for elements in transactions['results'] if elements['type'] == "OUTFLOW" and elements['status'] == 'PROCESSED']
        
        total_inflow = sum(transaction['amount'] for transaction in inflow)
        total_ouflow = sum(transaction['amount'] for transaction in outlow)
        
        health = total_inflow - total_ouflow
        
        resutl = 'good financial health'
        
        if health < 0 :
            
            resutl = 'financial distress'
        
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder({"message":resutl}) )

    except Exception as error:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))