from sqlalchemy import Column, Integer, String, Float
from db.connection import Base

class Mortgage(Base):
    __tablename__ = 'mortgages'
    id = Column(Integer, primary_key=True, index=True)
    applicant_name = Column(String(100))
    income = Column(Float)
    loan_amount = Column(Float)
    duration_years = Column(Integer)
    credit_rating = Column(String(10))
