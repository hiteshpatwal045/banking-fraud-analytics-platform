from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.services.analytics_service import (
    get_branch_transactions,
    get_transaction_modes
)

router = APIRouter(
    prefix="/api/analytics",
    tags=["Analytics"]
)


@router.get("/branch-transactions")
def branch_transactions(
    db: Session = Depends(get_db)
):
    return get_branch_transactions(db)


@router.get("/transaction-modes")
def transaction_modes(
    db: Session = Depends(get_db)
):
    return get_transaction_modes(db)
