# following sample code from https://www.python-course.eu/python3_pytest.php
# pycharm pytest support - https://www.jetbrains.com/help/pycharm/pytest.html
# TDD - https://www.tutorialspoint.com/software_testing_dictionary/test_driven_development.htm
from factorial import *


def test_odd_factorial():
    assert factorial(3) == 6
    assert factorial(5) == 120


def test_even_factorial():
    assert factorial(2) == 2
    assert factorial(4) == 24


def test_factorial_of_one():
    assert factorial(1) == 1


def test_sum_of_two_numbers():
    assert sum_of_two_number(1, 2) == 3


def test_difference_of_two_numbers():
    assert difference_of_two_numbers(3,2) == 1
