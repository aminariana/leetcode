import pytest
from UniqueNumberOfOccurrences.python import unique_occurrences

class TestUniqueOccurrences:
    def test_unique_occurrences(self):
        assert unique_occurrences.uniqueOccurrences([1,2,2,1,1,3])

    def test_same_occurrences(self):
        assert not unique_occurrences.uniqueOccurrences([1,2])

    def test_negative_but_unique_occurrences(self):
        assert unique_occurrences.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
