def calculate_credit_rating(income, loan_amount, duration):
    try:
        ratio = loan_amount / income
        if ratio < 0.2:
            return "AAA"
        elif ratio < 0.4:
            return "AA"
        elif ratio < 0.6:
            return "A"
        elif ratio < 0.8:
            return "BBB"
        else:
            return "BB"
    except ZeroDivisionError:
        return "Invalid"
