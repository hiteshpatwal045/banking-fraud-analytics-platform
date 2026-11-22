import pandas as pd

VALID_TRANSACTION_TYPES = ["CREDIT", "DEBIT"]
VALID_TRANSACTION_MODES = [
  "UPI",
  "ATM",
  "Debit Card",
  "Credit Card",
  "Net Banking",
  "Mobile Banking"
]


def validate_transactions(transactions: pd.DataFrame, account_balances: dict) -> tuple[pd.DataFrame, pd.DataFrame]:
  """Split transactions into valid rows and rejected rows."""
  valid_rows = []
  rejected_rows = []
  seen_ids = set()

  for row in transactions.to_dict("records"):
    reason = ""

    amount = pd.to_numeric(row["transaction_amount"], errors="coerce")
    txn_date = pd.to_datetime(row["transaction_date"], errors="coerce")

    if row["transaction_id"] == "":
      reason = "transaction_id is missing"
    elif row["transaction_id"] in seen_ids:
      reason = "duplicate transaction_id"
    elif row["account_id"] == "":
      reason = "account_id is missing"
    elif row["account_id"] not in account_balances:
      reason = "account does not exist"
    elif pd.isna(amount) or amount <= 0:
      reason = "transaction_amount must be greater than zero"
    elif row["transaction_type"] not in VALID_TRANSACTION_TYPES:
      reason = "invalid transaction_type"
    elif row["transaction_mode"] not in VALID_TRANSACTION_MODES:
      reason = "invalid transaction_mode"
    elif pd.isna(txn_date):
      reason = "invalid transaction_date"
    elif row["transaction_type"] == "DEBIT" and amount > account_balances[row["account_id"]]:
      reason = "debit amount exceeds available balance"

    seen_ids.add(row["transaction_id"])

    if reason == "":
      valid_rows.append(row)
    else:
      row["rejection_reason"] = reason
      rejected_rows.append(row)

  return pd.DataFrame(valid_rows), pd.DataFrame(rejected_rows)