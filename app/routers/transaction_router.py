from datetime import date

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.transaction_schema import (
    TransactionCreate,
    TransactionResponse
)

from app.services.transaction_service import (
    get_all_transactions,
    get_transaction_by_id,
    get_transactions_by_account,
    get_transactions_by_date,
    get_high_value_transactions,
    get_suspicious_transactions,
    create_transaction
)

router = APIRouter(
    prefix="/api/transactions",
    tags=["Transactions"]
)


@router.get(
    "/",
    response_model=list[TransactionResponse]
)
def fetch_transactions(
    db: Session = Depends(get_db)
):
    return get_all_transactions(db)


@router.get(
    "/high-value",
    response_model=list[TransactionResponse]
)
def high_value_transactions(
    db: Session = Depends(get_db)
):
    return get_high_value_transactions(db)


@router.get(
    "/suspicious",
    response_model=list[TransactionResponse]
)
def suspicious_transactions(
    db: Session = Depends(get_db)
):
    return get_suspicious_transactions(db)


@router.get(
    "/account/{account_id}",
    response_model=list[TransactionResponse]
)
def account_transactions(
    account_id: str,
    db: Session = Depends(get_db)
):
    return get_transactions_by_account(
        account_id,
        db
    )


@router.get(
    "/date/{transaction_date}",
    response_model=list[TransactionResponse]
)
def date_transactions(
    transaction_date: date,
    db: Session = Depends(get_db)
):
    return get_transactions_by_date(
        transaction_date,
        db
    )


@router.get(
    "/{transaction_id}",
    response_model=TransactionResponse
)
def fetch_transaction(
    transaction_id: str,
    db: Session = Depends(get_db)
):

    transaction = get_transaction_by_id(
        transaction_id,
        db
    )

    if transaction is None:

        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )

    return transaction


@router.post(
    "/",
    response_model=TransactionResponse
)
def add_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db)
):

    return create_transaction(
        transaction,
        db
    )