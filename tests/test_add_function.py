import pytest
import src.my_functions as my_functions


def test_add_integer_sum():
    result = my_functions.add(2,2)
    assert result == 4

def test_add_float_sum():
    result = my_functions.add(2.75,2.25)
    assert result == 5.0

def test_concatenate_strings():
    result = my_functions.add("i like ", "burgers")
    assert result == "i like burgers"