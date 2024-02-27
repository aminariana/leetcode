import pytest
from MaxConsecutiveOnes.python.longest_ones import longestOnes

class TestLongestOnes:
    def test_two(self):
        assert 6 == longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)

    def test_three(self):
        assert 10 == longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)
