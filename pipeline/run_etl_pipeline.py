import json
import logging
from datetime import datetime

from pipeline.extract import extract_data
from pipeline.validators.branch_validator import validate_branches
from pipeline.validators.customer_validator import validate_customers
from pipeline.validators.account_validator import validate_accounts
from pipeline.validators.transaction_validator import validate_transactions
from pipeline.validators.loan_validator import validate_loans
from pipeline.rejected_handler import save_rejected_records
from pipeline.transform import transform_data, build_enterprise_dataset
from pipeline.load import load_data

logging.basicConfig(
  filename="logs/pipeline.log",
  level=logging.INFO,
  format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():
  print("Starting Banking Data Pipeline....")
  run_id = datetime.now().strftime("RUN_%Y%m%d_%H%M%S")
  logging.info("Pipeline started: " + run_id)

  try:
    print("Step 1. Extracting Data....")
    customers, accounts, branches, transactions, loans = extract_data()

    print("Step 2. Validating Data....")
    valid_branches, rejected_branches = validate_branches(branches)
    valid_customers, rejected_customers = validate_customers(customers)

    valid_customer_ids = set(valid_customers["customer_id"])
    valid_branch_ids = set(valid_branches["branch_id"])
    valid_accounts, rejected_accounts = validate_accounts(accounts, valid_customer_ids, valid_branch_ids)

    account_balances = dict(zip(valid_accounts["account_id"], valid_accounts["balance"].astype(float)))
    valid_transactions, rejected_transactions = validate_transactions(transactions, account_balances)

    valid_loans, rejected_loans = validate_loans(loans, valid_customer_ids)

    print("Step 3. Saving Rejected Records....")
    save_rejected_records({
      "customers": rejected_customers,
      "accounts": rejected_accounts,
      "branches": rejected_branches,
      "transactions": rejected_transactions,
      "loans": rejected_loans
    }, run_id)

    print("Step 4. Transforming Data....")
    valid_customers, valid_accounts, valid_transactions, valid_loans = transform_data(
      valid_customers, valid_accounts, valid_transactions, valid_loans
    )
    build_enterprise_dataset(valid_customers, valid_accounts, valid_branches, valid_transactions)


    print("Step 5. Loading Data into MySQL....")
    load_data(valid_customers, valid_accounts, valid_branches, valid_transactions, valid_loans)

    result = {
      "status": "SUCCESS",
      "customers_received": len(customers),
      "customers_loaded": len(valid_customers),
      "customers_rejected": len(rejected_customers),
      "accounts_received": len(accounts),
      "accounts_loaded": len(valid_accounts),
      "accounts_rejected": len(rejected_accounts),
      "branches_received": len(branches),
      "branches_loaded": len(valid_branches),
      "branches_rejected": len(rejected_branches),
      "transactions_received": len(transactions),
      "transactions_loaded": len(valid_transactions),
      "transactions_rejected": len(rejected_transactions),
      "loans_received": len(loans),
      "loans_loaded": len(valid_loans),
      "loans_rejected": len(rejected_loans),
      "status_message": "Banking Data Pipeline completed successfully"
    }
    logging.info("Pipeline finished")

  except Exception as error:
    logging.error("Pipeline failed: " + str(error))
    result = {"status": "FAILED", "status_message": str(error)}

  print(json.dumps(result, indent=4))
  return result


if __name__ == "__main__":
  run_pipeline()