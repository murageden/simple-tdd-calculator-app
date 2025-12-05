#test_calculator_app.py
from calculator_app import calc_sum, calc_multiply, calc_divide, calc_subtract


def test_sum_of_numbers():
    assert calc_sum(3,4) == 7

def test_multiplication_of_numbers():
    assert calc_multiply(6,9) == 54

def test_division_of_numbers():
    assert calc_divide(7,2) == 3

def test_subtraction_of_numbers():
    assert calc_subtract(10,1) == 9

