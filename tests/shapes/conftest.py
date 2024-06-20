import pytest
import src.shapes as shape

@pytest.fixture
def base_rectangle():
    return shape.Rectangle(15, 5)

@pytest.fixture
def weird_rectangle():
    return shape.Rectangle(6,5)