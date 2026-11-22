from sqlalchemy import func

from app.models.branch import Branch
from app.models.account import Account
from app.models.transaction import Transaction


def get_branch_transactions(db):

    records = (
        db.query(
            Branch.branch_name,
            func.sum(
                Transaction.transaction_amount
            ).label("total_amount")
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

    result = []

    for row in records:

        result.append(
            {
                "branch_name": row.branch_name,
                "total_amount": float(row.total_amount)
            }
        )

    return result


def get_transaction_modes(db):

    records = (
        db.query(
            Transaction.transaction_mode,
            func.count().label("total")
        )
        .group_by(
            Transaction.transaction_mode
        )
        .all()
    )

    result = []

    for row in records:

        result.append(
            {
                "transaction_mode": row.transaction_mode,
                "total": row.total
            }
        )

    return result