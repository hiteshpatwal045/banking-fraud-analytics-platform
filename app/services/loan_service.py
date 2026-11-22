from app.models.loan import Loan


def get_all_loans(db):

    return db.query(Loan).all()


def get_loan_by_id(loan_id, db):

    return (
        db.query(Loan)
        .filter(
            Loan.loan_id == loan_id
        )
        .first()
    )


def get_loans_by_customer(
    customer_id,
    db
):

    return (
        db.query(Loan)
        .filter(
            Loan.customer_id == customer_id
        )
        .all()
    )