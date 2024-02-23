import pytest
from HouseRobber.python import house_robber

class TestHouseRobber:
    def test_empty(self):
        assert 0 == house_robber.rob([])

    def test_zero(self):
        assert 0 == house_robber.rob([0])

    def test_non_zero(self):
        assert 2 == house_robber.rob([2])

    def test_example1(self):
        assert 4 == house_robber.rob([1,2,3,1])

    def test_example2(self):
        assert 12 == house_robber.rob([2,7,9,3,1])

    def test_rich(self):
        assert 401 == house_robber.rob([400, 2, 1])

    def test_ambiguous(self):
        assert 13 == house_robber.rob([3, 1, 3, 1, 3, 7])

    def test_unambiguous(self):
        assert 14 == house_robber.rob([3, 1, 3, 1, 3, 7, 0, 1])
