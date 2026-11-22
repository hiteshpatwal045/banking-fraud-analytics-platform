from app.models.customer import Customer


def get_all_customers(db):
    return db.query(Customer).all()


def get_customer_by_id(customer_id, db):
    return (
        db.query(Customer)
        .filter(Customer.customer_id == customer_id)
        .first()
    )


def create_customer(customer_data, db):

    customer = Customer(**customer_data.model_dump())

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer


def update_customer(customer_id, customer_data, db):

    customer = get_customer_by_id(
        customer_id,
        db
    )

    if not customer:
        return None

    for key, value in customer_data.model_dump(
        exclude_unset=True
    ).items():

        setattr(customer, key, value)

    db.commit()
    db.refresh(customer)

    return customer


def delete_customer(customer_id, db):

    customer = get_customer_by_id(
        customer_id,
        db
    )

    if not customer:
        return False

    db.delete(customer)
    db.commit()

    return True