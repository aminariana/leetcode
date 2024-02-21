import pytest
from ContainerWithMostWater.python import solution

class TestContainer:
    def test_empty(self):
        assert 0 == solution.max_area([])

    def test_longer_side(self):
        assert 49 == solution.max_area([1,8,6,2,5,4,8,3,7])

    def test_unit_square(self):
        assert 1 == solution.max_area([1,1])
