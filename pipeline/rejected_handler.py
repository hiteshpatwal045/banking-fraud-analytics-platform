import os
from datetime import datetime


def save_rejected_records(rejected, run_id):
  os.makedirs("data/rejected", exist_ok=True)
  rejected_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  for name, df in rejected.items():
    df["rejected_at"] = rejected_at
    df["pipeline_run_id"] = run_id
    df.to_csv("data/rejected/rejected_" + name + ".csv", index=False)