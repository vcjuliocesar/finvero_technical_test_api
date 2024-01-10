from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import and_, case, func
from src.domain.models.account_entity import AccountEntity
from src.domain.models.transaction_entity import TransactionEntity
from src.infrastructure.config.connection import get_db
from src.infrastructure.repositories.interface.repositoty_interface import RepositoryInterface


class TransactionRepository(RepositoryInterface):

    def __init__(self, db: Session = Depends(get_db)) -> None:

        self.db = db

    def create(self, transaction: TransactionEntity) -> TransactionEntity:

        self.db.add(transaction)

        self.db.commit()

        return transaction

    def find_by(self, criteria: dict) -> TransactionEntity:

        return self.db.query(TransactionEntity).filter_by(**criteria).all()

    def find_one_by(self, criteria: dict) -> TransactionEntity:

        return self.db.query(TransactionEntity).filter_by(**criteria).first()

    def get(self):

        return self.db.query(TransactionEntity).all()

    def delete(self, transaction: TransactionEntity) -> None:

        self.db.delete(transaction)

        self.db.commit()

    def find_one_by_account_id(self,account_id):
        
        return self.db.query(AccountEntity).filter(AccountEntity.account_id == account_id).first()
        
    def get_income_and_expense(self, account_id: str):

        return self.db.query(
            func.sum(
                case(((TransactionEntity.type == 'INFLOW',
                     TransactionEntity.amount)), else_=0)
            )
            - func.sum(
                case(((TransactionEntity.type == 'OUTFLOW',
                     TransactionEntity.amount)), else_=0)
            )
        ).join(AccountEntity).filter(
            AccountEntity.account_id == account_id,
            TransactionEntity.status == 'PROCESSED'
        ).scalar()


    def get_balance(self, account_id):

        return self.db.query(
            func.sum(
                case(((TransactionEntity.type == 'INFLOW',
                     TransactionEntity.amount)), else_=0)
            )
            + func.sum(
                case(((TransactionEntity.type == 'OUTFLOW',
                     TransactionEntity.amount)), else_=0)
            )
        ).join(AccountEntity).filter(
            AccountEntity.account_id == account_id,
            TransactionEntity.status == 'PROCESSED'
        ).scalar()
