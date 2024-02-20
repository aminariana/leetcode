import pytest
from TrappingRainWater.python import solution

class TestSolution:
    def test_empty(self):
        assert 0 == solution.trap([])

    def test_hill(self):
        assert 0 == solution.trap([0, 1, 2, 1, 0])

    def test_bowl(self):
        assert 4 == solution.trap([2, 1, 0, 1, 2])

    def test_normal(self):
        assert 6 == solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
