import pytest
from MaximumNumberOfVowelsInASubstringOfGivenLength.python.max_vowels import maxVowels

class TestMaxVowels:
    def test_contiguous(self):
        assert 3 == maxVowels("abciiidef", 3)

    def test_cutoff(self):
        assert 2 == maxVowels("aeiou", 2)

    def test_insufficient(self):
        assert 2 == maxVowels("leetcode", 3)

    def test_singleton(self):
        assert 1 == maxVowels("a", 1)

    def test_disjoint_long_window(self):
        assert 4 == maxVowels("weallloveyou", 7)

    def test_base(self):
        assert 1 == maxVowels("ab", 2)

    def test_base_reverse(self):
        assert 1 == maxVowels("ba", 2)

    def test_middle(self):
        assert 3 == maxVowels("aabiiicoooo", 3)
