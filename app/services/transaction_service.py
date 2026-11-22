from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from app.models.transaction import Transaction


def get_transaction_category(amount):

    if amount >= 100000:
        return "HIGH VALUE"

    elif amount >= 50000:
        return "MEDIUM VALUE"

    return "NORMAL"


def get_risk_status(amount):

    if amount >= 200000:
        return "HIGH RISK"

    elif amount >= 100000:
        return "MEDIUM RISK"

    return "NORMAL"


def get_all_transactions(db):

    return db.query(Transaction).all()


def get_transaction_by_id(transaction_id, db):

    return (
        db.query(Transaction)
        .filter(
            Transaction.transaction_id == transaction_id
        )
        .first()
    )


def get_transactions_by_account(account_id, db):

    return (
        db.query(Transaction)
        .filter(
            Transaction.account_id == account_id
        )
        .all()
    )


def get_transactions_by_date(transaction_date, db):

    return (
        db.query(Transaction)
        .filter(
            Transaction.transaction_date == transaction_date
        )
        .all()
    )


def get_high_value_transactions(db):

    return (
        db.query(Transaction)
        .filter(
            Transaction.transaction_amount >= 100000
        )
        .all()
    )


def get_suspicious_transactions(db):

    return (
        db.query(Transaction)
        .filter(
            Transaction.risk_status.in_(
                ["MEDIUM RISK", "HIGH RISK"]
            )
        )
        .all()
    )


def create_transaction(transaction_data, db):

    transaction = Transaction(

        transaction_id=transaction_data.transaction_id,

        account_id=transaction_data.account_id,

        transaction_type=transaction_data.transaction_type,

        transaction_amount=transaction_data.transaction_amount,

        transaction_date=transaction_data.transaction_date,

        transaction_mode=transaction_data.transaction_mode,

        merchant_category=transaction_data.merchant_category,

        transaction_category=get_transaction_category(
            transaction_data.transaction_amount
        ),

        risk_status=get_risk_status(
            transaction_data.transaction_amount
        )
    )

    try:

        db.add(transaction)

        db.commit()

        db.refresh(transaction)

        return transaction

    except IntegrityError:

        db.rollback()

        raise HTTPException(
            status_code=400,
            detail="Transaction ID already exists"
        )