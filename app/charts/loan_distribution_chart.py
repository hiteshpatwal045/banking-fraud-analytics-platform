import os

import matplotlib.pyplot as plt
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.loan import Loan


def generate_loan_distribution_chart(db: Session):

    results = (
        db.query(
            Loan.loan_type,
            func.sum(Loan.loan_amount).label(
                "total_amount"
            )
        )
        .group_by(
            Loan.loan_type
        )
        .all()
    )

    if not results:
        return None

    loan_types = [
        row.loan_type
        for row in results
    ]

    amounts = [
        float(row.total_amount)
        for row in results
    ]

    os.makedirs("charts", exist_ok=True)

    chart_path = (
        "charts/loan_distribution.png"
    )

    plt.figure(figsize=(10, 6))

    plt.bar(
        loan_types,
        amounts,
        color="orange"
    )

    plt.title(
        "Loan Portfolio Distribution"
    )

    plt.xlabel("Loan Type")

    plt.ylabel("Total Loan Amount")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(chart_path)

    plt.close()

    return chart_path