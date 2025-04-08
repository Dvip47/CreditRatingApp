from flask import Blueprint, request, jsonify
from models import Mortgage  
from db.connection import get_db_session 
from credit_rating import calculate_credit_rating 

mortgage_routes = Blueprint('mortgage_routes', __name__)

@mortgage_routes.route('/mortgages', methods=['POST'])
def add_mortgage():
    data = request.get_json()
    session = get_db_session()
    try:
        rating = calculate_credit_rating(
            data['income'], data['loan_amount'], data['duration_years']
        )
        new_entry = Mortgage(
            applicant_name=data['applicant_name'],
            income=data['income'],
            loan_amount=data['loan_amount'],
            duration_years=data['duration_years'],
            credit_rating=rating
        )
        session.add(new_entry)
        session.commit()
        return jsonify({"message": "Mortgage added", "rating": rating}), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()

@mortgage_routes.route('/mortgages', methods=['GET'])
def get_mortgages():
    session = get_db_session()
    try:
        entries = session.query(Mortgage).all()
        result = [
            {
                "id": m.id,
                "applicant_name": m.applicant_name,
                "income": m.income,
                "loan_amount": m.loan_amount,
                "duration_years": m.duration_years,
                "credit_rating": m.credit_rating
            }
            for m in entries
        ]
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()
