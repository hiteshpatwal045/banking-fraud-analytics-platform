import os

import matplotlib.pyplot as plt
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.transaction import Transaction


def generate_daily_transaction_chart(db: Session):

    results = (
        db.query(
            Transaction.transaction_date,
            func.sum(Transaction.transaction_amount).label("total_amount")
        )
        .group_by(Transaction.transaction_date)
        .order_by(Transaction.transaction_date)
        .all()
    )

    if not results:
        return None

    dates = [row.transaction_date for row in results]

    amounts = [
        float(row.total_amount)
        for row in results
    ]

    os.makedirs("charts", exist_ok=True)

    chart_path = "charts/daily_transactions.png"

    plt.figure(figsize=(12, 6))

    plt.plot(
        dates,
        amounts,
        marker="o"
    )

    plt.title("Daily Transaction Trend")

    plt.xlabel("Transaction Date")

    plt.ylabel("Total Transaction Amount")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(chart_path)

    plt.close()

    return chart_path