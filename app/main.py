from fastapi import FastAPI
import app.models
from app.routers.customer_router import router as customer_router
from app.routers.account_router import router as account_router
from app.routers.branch_router import router as branch_router
from app.routers.transaction_router import router as transaction_router
from app.routers.loan_router import router as loan_router
from app.routers.analytics_router import router as analytics_router
from app.routers.chart_router import router as chart_router

app = FastAPI(
    title="Enterprise Banking Analytics Platform",
    version="1.0.0",
    description="Enterprise Banking Transaction, Customer and Fraud Analytics Platform"
)


app.include_router(customer_router)
app.include_router(account_router)
app.include_router(branch_router)
app.include_router(transaction_router)
app.include_router(loan_router)
app.include_router(analytics_router)
app.include_router(chart_router)


@app.get("/")
def home():
    return {
        "status": "SUCCESS",
        "message": "Enterprise Banking Analytics Platform Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "UP",
        "database": "CONNECTED"
    }