from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.charts.branch_transaction_chart import (
    generate_branch_transaction_chart
)

from app.charts.transaction_mode_chart import (
    generate_transaction_mode_chart
)

from app.charts.daily_transaction_chart import (
    generate_daily_transaction_chart
)

from app.charts.loan_distribution_chart import (
    generate_loan_distribution_chart
)

from app.charts.risk_analysis_chart import (
    generate_risk_analysis_chart
)

router = APIRouter(
    prefix="/api/charts",
    tags=["Charts"]
)


@router.get("/branch-transactions")
def branch_transactions_chart(
    db: Session = Depends(get_db)
):
    chart_path = generate_branch_transaction_chart(db)

    if not chart_path:
        raise HTTPException(
            status_code=404,
            detail="No data found"
        )

    return FileResponse(
        path=chart_path,
        media_type="image/png",
        filename="branch_transactions.png"
    )


@router.get("/transaction-modes")
def transaction_modes_chart(
    db: Session = Depends(get_db)
):
    chart_path = generate_transaction_mode_chart(db)

    if not chart_path:
        raise HTTPException(
            status_code=404,
            detail="No data found"
        )

    return FileResponse(
        path=chart_path,
        media_type="image/png",
        filename="transaction_modes.png"
    )


@router.get("/daily-transactions")
def daily_transactions_chart(
    db: Session = Depends(get_db)
):
    chart_path = generate_daily_transaction_chart(db)

    if not chart_path:
        raise HTTPException(
            status_code=404,
            detail="No data found"
        )

    return FileResponse(
        path=chart_path,
        media_type="image/png",
        filename="daily_transactions.png"
    )


@router.get("/loan-distribution")
def loan_distribution_chart(
    db: Session = Depends(get_db)
):
    chart_path = generate_loan_distribution_chart(db)

    if not chart_path:
        raise HTTPException(
            status_code=404,
            detail="No data found"
        )

    return FileResponse(
        path=chart_path,
        media_type="image/png",
        filename="loan_distribution.png"
    )


@router.get("/risk-analysis")
def risk_analysis_chart(
    db: Session = Depends(get_db)
):
    chart_path = generate_risk_analysis_chart(db)

    if not chart_path:
        raise HTTPException(
            status_code=404,
            detail="No data found"
        )

    return FileResponse(
        path=chart_path,
        media_type="image/png",
        filename="risk_analysis.png"
    )