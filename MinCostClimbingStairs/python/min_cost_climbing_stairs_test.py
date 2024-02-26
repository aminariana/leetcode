import pytest
from MinCostClimbingStairs.python.min_cost_climbing_stairs import minCostClimbingStairs

class TestMinCostClimbingStairs:
    def test_double_skip(self):
        assert 15 == minCostClimbingStairs([10,15,20])

    def test_inconsistent_skip(self):
        assert 6 == minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
