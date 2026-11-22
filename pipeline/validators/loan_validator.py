import pandas as pd

VALID_LOAN_TYPES = ["Home Loan","Personal Loan","Car Loan","Education Loan","Business Loan"]
VALID_LOAN_STATUS = ["Active", "Closed", "Defaulted", "Approved"]


def validate_loans(loans: pd.DataFrame, valid_customer_ids: set) -> tuple[pd.DataFrame, pd.DataFrame]:
  """Split loans into valid rows and rejected rows."""
  valid_rows = []
  rejected_rows = []
  seen_ids = set()

  for row in loans.to_dict("records"):
    reason = ""

    amount = pd.to_numeric(row["loan_amount"], errors="coerce")
    rate = pd.to_numeric(row["interest_rate"], errors="coerce")

    if row["loan_id"] == "":
      reason = "loan_id is missing"
    elif row["loan_id"] in seen_ids:
      reason = "duplicate loan_id"
    elif row["customer_id"] == "":
      reason = "customer_id is missing"
    elif row["customer_id"] not in valid_customer_ids:
      reason = "customer does not exist"
    elif pd.isna(amount) or amount <= 0:
      reason = "loan_amount must be greater than zero"
    elif pd.isna(rate) or rate <= 0:
      reason = "interest_rate must be greater than zero"
    elif row["loan_type"] not in VALID_LOAN_TYPES:
      reason = "invalid loan_type"
    elif row["loan_status"] not in VALID_LOAN_STATUS:
      reason = "invalid loan_status"

    seen_ids.add(row["loan_id"])

    if reason == "":
      valid_rows.append(row)
    else:
      row["rejection_reason"] = reason
      rejected_rows.append(row)

  return pd.DataFrame(valid_rows), pd.DataFrame(rejected_rows)