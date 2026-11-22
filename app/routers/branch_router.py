from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.services.branch_service import *

router = APIRouter(
    prefix="/api/branches",
    tags=["Branches"]
)


@router.get("/")
def branches(
    db: Session = Depends(get_db)
):
    return get_all_branches(db)


@router.get("/{branch_id}")
def branch(
    branch_id: str,
    db: Session = Depends(get_db)
):
    return get_branch_by_id(
        branch_id,
        db
    )


@router.get("/city/{city}")
def city_branches(
    city: str,
    db: Session = Depends(get_db)
):
    return get_branches_by_city(
        city,
        db
    )