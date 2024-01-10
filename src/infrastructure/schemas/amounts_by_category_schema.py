from ast import List
from pydantic import BaseModel
from sqlalchemy import Transaction
from src.infrastructure.schemas.transaction_schema import TransactionSchema


class AmmounstByCategorySchema(TransactionSchema):
    pass
    