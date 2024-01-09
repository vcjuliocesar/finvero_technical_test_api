# from src.domain.models.account_entity import AccountEntity
# from src.domain.models.institution_entity import InstitutionEntity
# from src.domain.models.balance_entity import BalanceEntity
# from src.domain.models.loan_data_entity import LoanDataEntity
# from src.domain.models.credit_data_entity import CreditDataEntity
# from src.domain.models.transaction_entity import TransactionEntity
# from src.infrastructure.config.connection import get_db


# def insert_account_data(data):

#     db_session = next(get_db())

#     for item in data['results']:

#         institution = InstitutionEntity(
#             name=item['institution']['name'], type=item['institution']['type'])

#         exits = db_session.query(InstitutionEntity).filter_by(
#             name=item['institution']['name'], type=item['institution']['type']).first()

#         if not exits:

#             db_session.add(institution)

#             db_session.commit()

#         if not (db_session.query(AccountEntity).filter_by(account_id=item['id']).first()):
#             account = AccountEntity(
#                 account_id=item['id'],
#                 link=item['link'],
#                 currency=item['currency'],
#                 category=item['category'],
#                 type=item['type'],
#                 number=item['number'],
#                 agency=item['agency'],
#                 internal_identification=item['internal_identification'],
#                 public_identification_name=item['public_identification_name'],
#                 public_identification_value=item['public_identification_value'],
#                 name=item['name'],
#                 last_accessed_at=item['last_accessed_at'],
#                 balance_type=item['balance_type'],
#                 bank_product_id=item['bank_product_id'],
#                 institution_id=exits.id
#             )

#             db_session.add(account)

#             db_session.commit()

#             balance = BalanceEntity(
#                 current=item['balance']['current'],
#                 available=item['balance']['available'],
#                 account_id=account.id
#             )

#             db_session.add(balance)

#             db_session.commit()

#             if item['credit_data'] is not None:
#                 credit_data = CreditDataEntity(
#                     collected_at=item['credit_data']['collected_at'],
#                     credit_limit=item['credit_data']['credit_limit'],
#                     cutting_date=item['credit_data']['cutting_date'],
#                     next_payment_date=item['credit_data']['next_payment_date'],
#                     minimum_payment=item['credit_data']['minimum_payment'],
#                     monthly_payment=item['credit_data']['monthly_payment'],
#                     no_interest_payment=item['credit_data']['no_interest_payment'],
#                     last_payment_date=item['credit_data']['last_payment_date'],
#                     last_period_balance=item['credit_data']['last_period_balance'],
#                     interest_rate=item['credit_data']['interest_rate'],
#                     account_id=account.id
#                 )

#                 db_session.add(credit_data)

#                 db_session.commit()

            


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
