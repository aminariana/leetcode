from ReverseVowelsOfAString.python.reverse_vowels import reverseVowels

class TestReverseVowels:
    def test_single_consonant(self):
        assert "x" == reverseVowels("x")

    def test_single_vowel(self):
        assert "o" == reverseVowels("o")

    def test_consonants_do_not_swap(self):
        assert "xy" == reverseVowels("xy")

    def test_vowels_swap(self):
        assert "oi" == reverseVowels("io")

    def test_capital_vowels_swap(self):
        assert "IAllm" == reverseVowels("AIllm")

    def test_normal_word(self):
        assert "holle" == reverseVowels("hello")

    def test_many_vowels_word(self):
        assert "leotcede" == reverseVowels("leetcode")
