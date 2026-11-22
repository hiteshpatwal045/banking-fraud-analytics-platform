import re
import pandas as pd
VALID_CUSTOMER_TYPES = ["Regular", "Premium", "Corporate"]
# Validate customers


def validate_customers(customers: pd.DataFrame) -> tuple[pd.DataFrame,pd.DataFrame]:
  """Split customers into valid rows and rejected rows."""
  valid_rows = []
  rejected_rows = []
  seen_ids = set()

  for row in customers.to_dict("records"):
    reason = ""

    if row["customer_id"] == "":
      reason = "customer_id is missing"
    elif row["customer_id"] in seen_ids:
      reason = "duplicate customer_id"
    elif row["customer_name"] == "":
      reason = "customer_name is missing"
    elif not re.match(r"^[\w.\-]+@[\w\-]+\.[A-Za-z]{2,}$", row["email"]):
      reason = "invalid email"
    elif not re.fullmatch(r"[6-9][0-9]{9}", row["mobile"]):
      reason = "invalid mobile number"
    elif row["customer_type"] not in VALID_CUSTOMER_TYPES:
      reason = "invalid customer_type"

    seen_ids.add(row["customer_id"])

    if reason == "":
      valid_rows.append(row)
    else:
      row["rejection_reason"] = reason
      rejected_rows.append(row)

  return pd.DataFrame(valid_rows), pd.DataFrame(rejected_rows)