from app.models.account import Account


def get_all_accounts(db):
    return db.query(Account).all()


def get_account_by_id(account_id, db):
    return (
        db.query(Account)
        .filter(Account.account_id == account_id)
        .first()
    )


def get_accounts_by_customer(customer_id, db):
    return (
        db.query(Account)
        .filter(Account.customer_id == customer_id)
        .all()
    )


def create_account(account_data, db):

    account = Account(
        account_id=account_data.account_id,
        customer_id=account_data.customer_id,
        account_type=account_data.account_type,
        branch_id=account_data.branch_id,
        balance=account_data.balance,
        opening_date=account_data.opening_date,
        account_status=account_data.account_status
    )

    db.add(account)
    db.commit()
    db.refresh(account)

    return account


def update_account(account_id, account_data, db):

    account = get_account_by_id(account_id, db)

    if not account:
        return None

    if account_data.account_type is not None:
        account.account_type = account_data.account_type

    if account_data.branch_id is not None:
        account.branch_id = account_data.branch_id

    if account_data.balance is not None:
        account.balance = account_data.balance

    if account_data.account_status is not None:
        account.account_status = account_data.account_status

    db.commit()
    db.refresh(account)

    return account