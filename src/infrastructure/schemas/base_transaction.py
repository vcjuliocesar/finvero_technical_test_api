from datetime import datetime
from pydantic import BaseModel, Field


class BaseTransaction(BaseModel):

    transaction_id :str

    category :str

    subcategory:str

    type :str

    amount:float

    status :str

    balance :float

    currency :str

    reference :str

    description :str

    collected_at:datetime

    observations:str

    accounting_date:datetime

    internal_identification :str

    created_at:datetime

    account_id:int

