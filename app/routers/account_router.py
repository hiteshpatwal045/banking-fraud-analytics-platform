from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.account_schema import (
    AccountCreate,
    AccountUpdate,
    AccountResponse
)

from app.services.account_service import (
    get_all_accounts,
    get_account_by_id,
    get_accounts_by_customer,
    create_account,
    update_account
)

router = APIRouter(
    prefix="/api/accounts",
    tags=["Accounts"]
)


@router.get(
    "/",
    response_model=list[AccountResponse]
)
def fetch_accounts(
    db: Session = Depends(get_db)
):
    return get_all_accounts(db)


@router.get(
    "/{account_id}",
    response_model=AccountResponse
)
def fetch_account(
    account_id: str,
    db: Session = Depends(get_db)
):
    account = get_account_by_id(account_id, db)

    if account is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return account


@router.get("/customer/{customer_id}")
def fetch_customer_accounts(
    customer_id: str,
    db: Session = Depends(get_db)
):
    accounts = get_accounts_by_customer(
        customer_id,
        db
    )

    if not accounts:
        raise HTTPException(
            status_code=404,
            detail="No accounts found for this customer"
        )

    return accounts


@router.post(
    "/",
    response_model=AccountResponse
)
def add_account(
    account: AccountCreate,
    db: Session = Depends(get_db)
):
    return create_account(account, db)


@router.put(
    "/{account_id}",
    response_model=AccountResponse
)
def edit_account(
    account_id: str,
    account: AccountUpdate,
    db: Session = Depends(get_db)
):
    updated_account = update_account(
        account_id,
        account,
        db
    )

    if updated_account is None:
        raise HTTPException(
            status_code=404,
            detail="Account not found"
        )

    return updated_account