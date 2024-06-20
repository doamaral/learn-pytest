import pytest
import math
from src.shapes import Circle

# Using a Class to handle tests

class TestCircle:

    def setup_method(self, method):
        print(f"setting up {method}")
        self.circle = Circle(5)
    
    def teardown_method(self, method):
        print(f"tearing down up {method}")

    def test_area_calc(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
    
    def test_perimeter_calc(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius