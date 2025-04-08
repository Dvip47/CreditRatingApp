import unittest
from credit_rating import calculate_credit_rating

class TestCreditRating(unittest.TestCase):
    def test_high_income(self):
        self.assertEqual(calculate_credit_rating(100000, 10000, 5), "AAA")

    def test_medium_income(self):
        self.assertEqual(calculate_credit_rating(50000, 20000, 5), "A")

    def test_zero_income(self):
        self.assertEqual(calculate_credit_rating(0, 10000, 5), "Invalid")
