from RomanToInteger.python.roman_to_int import romanToInt

class TestRomanToInt:
    def test_III(self):
        assert 3 == romanToInt("III")

    def test_LVIII(self):
        assert 58 == romanToInt("LVIII")

    def test_MCMXCIV(self):
        assert 1994 == romanToInt("MCMXCIV")
