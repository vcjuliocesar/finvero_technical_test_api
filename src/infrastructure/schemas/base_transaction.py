from datetime import datetime
from pydantic import BaseModel, Field


class BaseTransaction(BaseModel):

    transaction_id :str = Field("0644634a-696e-42df-95e1-c05772d9a6ab",title="transaction_id")

    category :str = Field("Income & Payments",title="category")

    subcategory:str = Field("null",title="subcategory")

    type :str = Field("INFLOW",title="type")

    amount:float = Field("380.03",title="amount")

    status :str = Field("PROCESSED",title="status")

    balance :float = Field("25645.5",title="balance")

    currency :str = Field("MXN",title="currency")

    reference :str = Field("1128",title="reference")

    description :str = Field("DISPERSION",title="reference")

    collected_at:datetime = Field("2024-01-07T21:55:58.681926Z",title="collected_at")

    observations:str = Field("null",title="observations")

    accounting_date:datetime = Field("2023-12-28T07:36:31",title="accounting_date")

    internal_identification :str = Field("51d312e3",title="internal_identification")

    created_at:datetime = Field("2024-01-07T21:58:47.336358Z",title="created_at")

    account_id:int = Field("1",title="account_id")

