from app.models.branch import Branch


def get_all_branches(db):
    return db.query(Branch).all()


def get_branch_by_id(branch_id, db):

    return (
        db.query(Branch)
        .filter(
            Branch.branch_id == branch_id
        )
        .first()
    )


def get_branches_by_city(city, db):

    return (
        db.query(Branch)
        .filter(
            Branch.city == city
        )
        .all()
    )