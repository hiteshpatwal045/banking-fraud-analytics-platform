from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.services.loan_service import *

router = APIRouter(
    prefix="/api/loans",
    tags=["Loans"]
)


@router.get("/")
def loans(
    db: Session = Depends(get_db)
):
    return get_all_loans(db)


@router.get("/{loan_id}")
def loan(
    loan_id: str,
    db: Session = Depends(get_db)
):
    return get_loan_by_id(
        loan_id,
        db
    )


@router.get("/customer/{customer_id}")
def customer_loans(
    customer_id: str,
    db: Session = Depends(get_db)
):
    return get_loans_by_customer(
        customer_id,
        db
    )