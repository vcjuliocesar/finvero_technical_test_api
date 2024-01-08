from fastapi import FastAPI, Depends, HTTPException, status
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
from src.presentation.data.data import insert_account_data, insert_transactions_data
from collections import defaultdict
from functools import reduce

app = FastAPI()


async def startup_event():

    instance = Belvo()

    # transactions = await instance.post_retrieve_transactions()

    # accounts = await instance.post_retrieve_accounts()

    # if transactions == 201 and accounts == 201:

    # transaction_list = await instance.get_transactions()

    # account_list = await instance.get_accounts()

    # insert_account_data(account_list)
    # insert_transactions_data(transaction_list)
    #


async def shutdown_event():
    print("shut down app...")

app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)


@app.get("/transactions", status_code=status.HTTP_200_OK)
async def get_transactions(belvo: Belvo = Depends()):
    try:

        transactions = await belvo.get_transactions()

        transactions['results'] = [element for element in transactions['results']
                   if element.get("category") == "Income & Payments"]
        
        transactions['results'] = [
            {**item, 'account': item['account']['id']} for item in transactions['results']]

        transactions['results'] = list(map(lambda x: {k: v for k, v in x.items(
        ) if k not in ('merchant')}, transactions['results']))
        
        return JSONResponse(status_code=status.HTTP_200_OK, content=transactions['results'])

    except Exception as error:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))


@app.get("/accounts", status_code=status.HTTP_200_OK)
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


@app.get("/amounts_by_category", status_code=status.HTTP_200_OK)
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
        
        return JSONResponse(status_code=status.HTTP_200_OK, content=transactions['results'])

    except Exception as error:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))


@app.get("/income_and_expense_analysis", status_code=status.HTTP_200_OK)
async def get_income_and_expense_analysis(belvo: Belvo = Depends()):
    try:
        user_id ="9cf598dc-3b6c-43e6-9c72-94b305d7837c"
        transactions = await belvo.get_transactions()
        
        transactions['results'] = [
            {**item, 'account': item['account']['id']} for item in transactions['results']]
        
        transactions['results'] = list(map(lambda x: {k: v for k, v in x.items(
        ) if k not in ('merchant')}, transactions['results']))
        
        transactions['results'] = [element for element in transactions['results']
                   if element.get("account") == user_id]
        
        inflow = [elements for elements in transactions['results'] if elements['type'] == "INFLOW" and elements['status'] == 'PROCESSED']
        outlow = [elements for elements in transactions['results'] if elements['type'] == "OUTFLOW" and elements['status'] == 'PROCESSED']
        
        total_inflow = sum(transaction['amount'] for transaction in inflow)
        total_ouflow = sum(transaction['amount'] for transaction in outlow)
        print('total_inflow',total_inflow)
        print('total_ouflow',total_ouflow)
        health = total_inflow - total_ouflow
        
        resutl = 'good financial health'
        
        if health < 0 :
            
            resutl = 'financial distress'
        
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message":resutl} )

    except Exception as error:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))

@app.get("/balance", status_code=status.HTTP_200_OK)
async def get_balance(belvo: Belvo = Depends()):
    try:
        user_id ="9cf598dc-3b6c-43e6-9c72-94b305d7837c"
        transactions = await belvo.get_transactions()
        
        transactions['results'] = [
            {**item, 'account': item['account']['id']} for item in transactions['results']]
        
        transactions['results'] = list(map(lambda x: {k: v for k, v in x.items(
        ) if k not in ('merchant')}, transactions['results']))
        
        transactions['results'] = [element for element in transactions['results']
                   if element.get("account") == user_id]
        
        inflow = [elements for elements in transactions['results'] if elements['type'] == "INFLOW" and elements['status'] == 'PROCESSED']
        outlow = [elements for elements in transactions['results'] if elements['type'] == "OUTFLOW" and elements['status'] == 'PROCESSED']
        
        total_inflow = sum(transaction['amount'] for transaction in inflow)
        total_ouflow = sum(transaction['amount'] for transaction in outlow)
        balance = total_inflow + total_ouflow
        
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message":f"balance ${balance}"} )

    except Exception as error:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
# init()
