import pytest
from DetermineIfTwoStringsAreClose.python import close_strings

class TestCloseStrings:
    def test_multi_swap(self):
        assert close_strings.closeStrings("abc", "bca")

    def test_length_difference(self):
        assert not close_strings.closeStrings("a", "aa")

    def test_frequency_swap_simple(self):
        assert close_strings.closeStrings("abb", "baa")

    def test_frequency_swap_complex(self):
        assert close_strings.closeStrings("cabbba", "abbccc")

    def test_reverse(self):
        assert close_strings.closeStrings("ab", "ba")

    def test_ambiguous(self):
        assert close_strings.closeStrings("abcb", "cbaa")

    def test_frequency_altered(self):
        assert not close_strings.closeStrings("aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff")
