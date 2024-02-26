import pytest
from MaximumAverageSubarrayI.python.find_max_average import findMaxAverage

class TestFindMaxAverage:
    def test_positives_and_negatives(self):
        assert 12.75000 == findMaxAverage([1,12,-5,-6,50,3], 4)

    def test_singleton(self):
        assert 5.00000 == findMaxAverage([5], 1)
