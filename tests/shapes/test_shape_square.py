import pytest
from src.shapes import Square

@pytest.mark.parametrize("side_length, expected_area", [(5, 25),(4, 16), (3, 9), (2, 4)])
def test_side_length_vs_expected_area(side_length, expected_area):
    assert Square(side_length).area() == expected_area