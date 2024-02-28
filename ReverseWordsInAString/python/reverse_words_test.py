from ReverseWordsInAString.python.reverse_words import reverseWords

class TestReverseWords:
    def test_sentence(self):
        assert "blue is sky the" == reverseWords("the sky is blue")

    def test_whitespace_outside(self):
        assert "world hello" == reverseWords("  hello world  ")

    def test_long_whitespace(self):
        assert "example good a" == reverseWords("a good   example")
