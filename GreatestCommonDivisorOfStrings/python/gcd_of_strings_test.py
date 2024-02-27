from GreatestCommonDivisorOfStrings.python.gcd_of_strings import gcdOfStrings

class TestGcdOfStrings:
    def test_halfling(self):
        assert "ABC" == gcdOfStrings("ABCABC", "ABC")

    def test_commonality(self):
        assert "AB" == gcdOfStrings("ABABAB", "ABAB")

    def test_nothing_in_common(self):
        assert "" == gcdOfStrings("LEET", "CODE")

    def test_non_repeating(self):
        assert "" == gcdOfStrings("ABCDEF", "ABC")

