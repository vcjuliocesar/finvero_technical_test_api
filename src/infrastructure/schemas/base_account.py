from datetime import datetime
from pydantic import BaseModel, Field


class BaseAccount(BaseModel):

    account_id: str

    link: str

    currency: str

    category: str

    type: str

    number: str

    agency: str

    internal_identification: str

    public_identification_name: str

    public_identification_value: str

    name: str

    last_accessed_at: datetime

    balance_type: str

    bank_product_id: str

    created_at: datetime

    collected_at: datetime
