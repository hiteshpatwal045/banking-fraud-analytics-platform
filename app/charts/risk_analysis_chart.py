import os

import matplotlib.pyplot as plt
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.transaction import Transaction


def generate_risk_analysis_chart(
    db: Session
):

    results = (
        db.query(
            Transaction.risk_status,
            func.count(
                Transaction.transaction_id
            ).label("count")
        )
        .group_by(
            Transaction.risk_status
        )
        .all()
    )

    if not results:
        return None

    risk_labels = [
        row.risk_status
        for row in results
    ]

    risk_counts = [
        row.count
        for row in results
    ]

    os.makedirs(
        "charts",
        exist_ok=True
    )

    chart_path = (
        "charts/risk_analysis.png"
    )

    plt.figure(figsize=(8, 8))

    plt.pie(
        risk_counts,
        labels=risk_labels,
        autopct="%1.1f%%"
    )

    plt.title(
        "Transaction Risk Analysis"
    )

    plt.savefig(chart_path)

    plt.close()

    return chart_path