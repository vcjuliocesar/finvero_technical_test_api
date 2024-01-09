from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.infrastructure.middlewares.jwt_bearer import JWTBearer
from src.infrastructure.service.belvo.belvo import Belvo
from collections import defaultdict

amounts_by_category_router = APIRouter(prefix="/api/v1",tags=["Amounts"])

@amounts_by_category_router.get("/amounts_by_category", status_code=status.HTTP_200_OK,dependencies=[Depends(JWTBearer())])
async def get_amounts_by_category(belvo: Belvo = Depends()):
    try:

        transactions = await belvo.get_transactions()

        transactions['results'] = [
            {**item, 'account': item['account']['id']} for item in transactions['results']]

        transactions['results'] = list(map(lambda x: {k: v for k, v in x.items(
        ) if k not in ('merchant')}, transactions['results']))

        transactions['results'] = sorted(transactions['results'], key=lambda x: x.get(
            "amount", 0.0) or 0.0, reverse=True)

        grouped_data = defaultdict(list)
        [grouped_data[item["category"].lower().replace(" ", "_") if item["category"] and item["category"].strip(
        ) else item["category"]].append(item) for item in transactions['results']]

        
        transactions['results'] = list(dict(category=category, transactions=group) for category, group in grouped_data.items())
        
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(transactions['results']))

    except Exception as error:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))