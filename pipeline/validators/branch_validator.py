import re

import pandas as pd


def validate_branches(branches: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
  """Split branches into valid rows and rejected rows."""
  valid_rows = []
  rejected_rows = []
  seen_ids = set()

  for row in branches.to_dict("records"):
    reason = ""

    if row["branch_id"] == "":
      reason = "branch_id is missing"
    elif row["branch_id"] in seen_ids:
      reason = "duplicate branch_id"
    elif row["branch_name"] == "":
      reason = "branch_name is missing"
    elif row["city"] == "":
      reason = "city is missing"
    elif row["manager_name"] == "":
      reason = "manager name is missing"
    elif not re.fullmatch(r"[A-Z]{4}0[A-Z0-9]{6}", row["ifsc_code"]):
      reason = "invalid IFSC code"

    seen_ids.add(row["branch_id"])

    if reason == "":
      valid_rows.append(row)
    else:
      row["rejection_reason"] = reason
      rejected_rows.append(row)

  return pd.DataFrame(valid_rows), pd.DataFrame(rejected_rows)