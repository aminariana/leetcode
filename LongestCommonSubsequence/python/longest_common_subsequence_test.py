from LongestCommonSubsequence.python.longest_common_subsequence import longestCommonSubsequence

class TestLongestCommonSubsequence:
    def test_typical(self):
        assert 3 == longestCommonSubsequence("abcde", "ace")

    def test_equal(self):
        assert 3 == longestCommonSubsequence("abc", "abc")

    def test_different(self):
        assert 0 == longestCommonSubsequence("abc", "def")

    def test_ambiguous(self):
        assert 3 == longestCommonSubsequence("cbbb", "babab")
