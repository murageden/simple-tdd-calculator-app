#testing_with_unitest
import unittest
from calculator_app import calc_sum, calc_multiply, calc_divide, calc_subtract


class MyTests(unittest.TestCase):
    def setUp(self):
        self.calc_sum = calc_sum(3,4)
        self.calc_multiply = calc_multiply(6,9)
        self.calc_divide = calc_divide(6,2)
        self.calc_subtract = calc_subtract(10,1)

    def test_sum(self):
        self.assertEqual(self.calc_sum, 7)

    def test_multiplication(self):
        self.assertEqual(self.calc_multiply, 54)

    def test_division(self):
        self.assertEqual(self.calc_divide, 3)

    def test_subtraction(self):
        self.assertEqual(self.calc_subtract, 9)

    def tearDown(self):
        self.calc_sum = None
        self.calc_multiply = None
        self.cal_divide = None
        self.calc_subtract = None


