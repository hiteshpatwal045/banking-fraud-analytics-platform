import os

import matplotlib.pyplot as plt
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.transaction import Transaction


def generate_transaction_mode_chart(db: Session):

    results = (
        db.query(
            Transaction.transaction_mode,
            func.count(Transaction.transaction_id).label("count")
        )
        .group_by(Transaction.transaction_mode)
        .all()
    )

    if not results:
        return None

    modes = [row.transaction_mode for row in results]
    counts = [row.count for row in results]

    os.makedirs("charts", exist_ok=True)

    chart_path = "charts/transaction_modes.png"

    plt.figure(figsize=(8, 8))

    plt.pie(
        counts,
        labels=modes,
        autopct="%1.1f%%"
    )

    plt.title("Transaction Mode Distribution")

    plt.savefig(chart_path)

    plt.close()

    return chart_path