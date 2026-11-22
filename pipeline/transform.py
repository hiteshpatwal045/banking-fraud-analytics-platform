import os
import pandas as pd


def get_transaction_category(amount):
  if amount >= 100000:
    return "HIGH VALUE"
  elif amount >= 50000:
    return "MEDIUM VALUE"
  else:
    return "NORMAL"


def get_risk_status(amount):
  if amount >= 200000:
    return "HIGH RISK"
  elif amount >= 100000:
    return "MEDIUM RISK"
  else:
    return "NORMAL"


def transform_data(customers, accounts, transactions, loans):
  customers["registration_date"] = pd.to_datetime(customers["registration_date"]).dt.date

  accounts["balance"] = accounts["balance"].astype(float)
  accounts["opening_date"] = pd.to_datetime(accounts["opening_date"]).dt.date

  transactions["transaction_amount"] = transactions["transaction_amount"].astype(float)
  transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"]).dt.date
  transactions["transaction_category"] = transactions["transaction_amount"].apply(get_transaction_category)
  transactions["risk_status"] = transactions["transaction_amount"].apply(get_risk_status)

  loans["loan_amount"] = loans["loan_amount"].astype(float)
  loans["interest_rate"] = loans["interest_rate"].astype(float)
  loans["loan_start_date"] = pd.to_datetime(loans["loan_start_date"]).dt.date

  return customers, accounts, transactions, loans


def build_enterprise_dataset(customers, accounts, branches, transactions):
  acc = accounts[["account_id", "customer_id", "branch_id", "account_type"]]
  cust = customers[["customer_id", "customer_name", "customer_type", "city"]]
  cust = cust.rename(columns={"city": "customer_city"})
  br = branches[["branch_id", "branch_name", "city", "state"]]
  br = br.rename(columns={"city": "branch_city"})

  enterprise = transactions.merge(acc, on="account_id", how="left")
  enterprise = enterprise.merge(cust, on="customer_id", how="left")
  enterprise = enterprise.merge(br, on="branch_id", how="left")

  os.makedirs("data/processed", exist_ok=True)
  enterprise.to_csv("data/processed/enterprise_transactions.csv", index=False)