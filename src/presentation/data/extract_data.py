from sqlalchemy import inspect
from src.domain.models.account_entity import AccountEntity
from src.domain.models.transaction_entity import TransactionEntity
from src.infrastructure.config.connection import get_db,get_settings

instance = get_settings()

engine = instance.get_engine()

inspector = inspect(engine)

def extract_data_on_startup(data):

    db_session = next(get_db())
    
    print("TableExists",inspector.has_table('account'))
    
    accounts = data['accounts']['results']
    transactions = data['transactions']['results']
    
    accounts = list(map(lambda x: {k: v for k, v in x.items(
    ) if k not in ('institution', 'balance')},  accounts))

    transactions = list(map(lambda x: {k: v for k, v in x.items(
         ) if k not in ('merchant','loan_data','credit_data')}, transactions))
    
    for item in accounts:

        account = AccountEntity(
            account_id=item['id'],
            link=item['link'],
            currency=item['currency'],
            category=item['category'],
            type=item['type'],
            number=item['number'],
            agency=item['agency'],
            internal_identification=item['internal_identification'],
            public_identification_name=item['public_identification_name'],
            public_identification_value=item['public_identification_value'],
            name=item['name'],
            last_accessed_at=item['last_accessed_at'],
            balance_type=item['balance_type'],
            bank_product_id=item['bank_product_id'],
        )
        
        account_exists = db_session.query(AccountEntity).filter_by(account_id=item['id']).first()
        
        if not account_exists:
            
            db_session.add(account)
            db_session.commit()

    
    for item in transactions:
        
        transaction = TransactionEntity(
            transaction_id=item['id'],
            category=item['category'],
            subcategory=item['subcategory'],
            type=item['type'],
            amount=item['amount'],
            status=item['status'],
            balance=item['balance'],
            currency=item['currency'],
            reference=item['reference'],
            description=item['description'],
            #collected_at=item['collected_at'],
            observations=item['observations'],
            accounting_date=item['accounting_date'],
            internal_identification =item['internal_identification'],
            #created_at=item['created_at'],
            account_id=db_session.query(AccountEntity).filter_by(account_id=item['account']['id']).first().id
            )
        #print(item['account']['id'])
        #print(db_session.query(AccountEntity).filter_by(account_id=item['account']['id']).first().id)
        transaction_exists = db_session.query(TransactionEntity).filter_by(transaction_id=item['id']).first()
        
        if not transaction_exists:
            
            db_session.add(transaction)
            db_session.commit()
# def insert_transactions_data(data):
#     db_session = next(get_db())

#     for item in data['results']:

#         account_id = db_session.query(AccountEntity).filter(
#             AccountEntity.account_id == item['account']['id']).first()

#         transaction = TransactionEntity(
#             transaction_id=item['id'],
#             category=item['category'],
#             subcategory=item['subcategory'],
#             type=item['type'],
#             amount=item['amount'],
#             status=item['status'],
#             balance=item['balance'],
#             currency=item['currency'],
#             reference=item['reference'],
#             description=item['description'],
#             #collected_at=item['collected_at'],
#             account_id=account_id.id
#         )

#         db_session.add(transaction)
#         db_session.commit()
