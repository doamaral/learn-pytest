import pytest
import src.shapes as shape

@pytest.fixture
def weird_rectangle():
    return shape.Rectangle(6,5)