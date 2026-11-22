from sqlalchemy import text

from app.database.connection import Base, engine

# models must be imported so the tables get created
from app.models.customer import Customer
from app.models.branch import Branch
from app.models.account import Account
from app.models.transaction import Transaction
from app.models.loan import Loan

def load_data(customers, accounts, branches, transactions, loans):
  Base.metadata.create_all(bind=engine)

  # clear old data (child tables first)
  with engine.begin() as conn:
    conn.execute(text("DELETE FROM transactions"))
    conn.execute(text("DELETE FROM loans"))
    conn.execute(text("DELETE FROM accounts"))
    conn.execute(text("DELETE FROM customers"))
    conn.execute(text("DELETE FROM branches"))

  # insert new data (parent tables first)
  branches.to_sql("branches", engine, if_exists="append", index=False)
  customers.to_sql("customers", engine, if_exists="append", index=False)
  accounts.to_sql("accounts", engine, if_exists="append", index=False)
  transactions.to_sql("transactions", engine, if_exists="append", index=False)
  loans.to_sql("loans", engine, if_exists="append", index=False)