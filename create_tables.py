from app.database.connection import Base, engine

from app.models.customer import Customer
from app.models.branch import Branch
from app.models.account import Account
from app.models.transaction import Transaction
from app.models.loan import Loan
from app.models.rejected_record import RejectedRecord

Base.metadata.create_all(bind=engine)

print("Tables created successfully")