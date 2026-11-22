import pandas as pd

VALID_ACCOUNT_TYPES = ["Savings", "Current", "Salary", "Business"]


def validate_accounts(accounts: pd.DataFrame, valid_customer_ids: set, valid_branch_ids: set) -> tuple[pd.DataFrame, pd.DataFrame]:
  """Split accounts into valid rows and rejected rows."""
  valid_rows = []
  rejected_rows = []
  seen_ids = set()

  for row in accounts.to_dict("records"):
    reason = ""

    balance = pd.to_numeric(row["balance"], errors="coerce")
    opening_date = pd.to_datetime(row["opening_date"], errors="coerce")

    if row["account_id"] == "":
      reason = "account_id is missing"
    elif row["account_id"] in seen_ids:
      reason = "duplicate account_id"
    elif row["customer_id"] == "":
      reason = "customer_id is missing"
    elif row["customer_id"] not in valid_customer_ids:
      reason = "customer does not exist"
    elif row["branch_id"] not in valid_branch_ids:
      reason = "branch does not exist"
    elif pd.isna(balance) or balance < 0:
      reason = "balance must not be negative"
    elif row["account_type"] not in VALID_ACCOUNT_TYPES:
      reason = "invalid account_type"
    elif pd.isna(opening_date):
      reason = "invalid opening_date"

    seen_ids.add(row["account_id"])

    if reason == "":
      valid_rows.append(row)
    else:
      row["rejection_reason"] = reason
      rejected_rows.append(row)

  return pd.DataFrame(valid_rows), pd.DataFrame(rejected_rows)