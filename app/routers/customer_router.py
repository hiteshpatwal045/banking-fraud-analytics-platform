from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.customer_schema import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse
)

from app.services.customer_service import *

router = APIRouter(
    prefix="/api/customers",
    tags=["Customers"]
)


@router.get(
    "/",
    response_model=list[CustomerResponse]
)
def customers(
    db: Session = Depends(get_db)
):
    return get_all_customers(db)


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse
)
def customer(
    customer_id: str,
    db: Session = Depends(get_db)
):

    customer = get_customer_by_id(
        customer_id,
        db
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@router.post(
    "/",
    response_model=CustomerResponse
)
def add_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    return create_customer(
        customer,
        db
    )


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse
)
def edit_customer(
    customer_id: str,
    customer: CustomerUpdate,
    db: Session = Depends(get_db)
):
    return update_customer(
        customer_id,
        customer,
        db
    )


@router.delete("/{customer_id}")
def remove_customer(
    customer_id: str,
    db: Session = Depends(get_db)
):

    status = delete_customer(
        customer_id,
        db
    )

    if not status:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return {
        "message": "Customer deleted successfully"
    }