import os

import matplotlib.pyplot as plt
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.branch import Branch
from app.models.account import Account
from app.models.transaction import Transaction


def generate_branch_transaction_chart(db: Session):

    results = (
        db.query(
            Branch.branch_name,
            func.sum(Transaction.transaction_amount).label(
                "total_amount"
            )
        )
        .join(
            Account,
            Branch.branch_id == Account.branch_id
        )
        .join(
            Transaction,
            Account.account_id == Transaction.account_id
        )
        .group_by(
            Branch.branch_name
        )
        .all()
    )

    if not results:
        return None

    branch_names = [row.branch_name for row in results]

    transaction_amounts = [
        float(row.total_amount)
        for row in results
    ]

    os.makedirs("charts", exist_ok=True)

    chart_path = (
        "charts/branch_transaction_chart.png"
    )

    plt.figure(figsize=(12, 6))

    plt.bar(
        branch_names,
        transaction_amounts,
        color="steelblue"
    )

    plt.title(
        "Branch Wise Transaction Value"
    )

    plt.xlabel("Branch Name")
    plt.ylabel(
        "Total Transaction Amount"
    )

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return chart_path