#Using functional approach with pytest.fixtures defined in conftest.py

def test_rectangle_area(weird_rectangle):
    assert weird_rectangle.area() == 5 * 6

def test_rectangle_perimeter(weird_rectangle):
    assert weird_rectangle.perimeter() == 2 * 5 + 2 * 6

def test_rectangles_equality(weird_rectangle, base_rectangle):
    assert base_rectangle != weird_rectangle