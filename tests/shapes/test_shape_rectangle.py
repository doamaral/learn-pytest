#Using functional approach with pytest.fixtures

def test_rectangle_area(weird_rectangle):
    assert weird_rectangle.area() == 5 * 6