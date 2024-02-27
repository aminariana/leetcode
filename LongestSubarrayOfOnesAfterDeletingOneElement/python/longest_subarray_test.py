import pytest
from LongestSubarrayOfOnesAfterDeletingOneElement.python.longest_subarray import longestSubarray

class TestLongestSubarray:
    def test_base_case_zero(self):
        assert 0 == longestSubarray([0])

    def test_base_case_one(self):
        assert 0 == longestSubarray([1])

    def test_single_delete(self):
        assert 3 == longestSubarray([1,1,0,1])

    def test_optimal_delete(self):
        assert 5 == longestSubarray([0,1,1,1,0,1,1,0,1])

    def test_unwanted_delete(self):
        assert 2 == longestSubarray([1,1,1])

