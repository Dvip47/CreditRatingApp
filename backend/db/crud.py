
def create_mortgage(session, data, rating):
    from models import Mortgage
    entry = Mortgage(
        applicant_name=data['applicant_name'],
        income=data['income'],
        loan_amount=data['loan_amount'],
        duration_years=data['duration_years'],
        credit_rating=rating
    )
    session.add(entry)
    session.commit()
    return entry