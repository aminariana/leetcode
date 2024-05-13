from IntegerToRoman.python.int_to_roman import intToRoman

class TestIntToRoman:
    def test_3749(self):
        assert "MMMDCCXLIX" == intToRoman(3749)

    def test_58(self):
        assert "LVIII" == intToRoman(58)

    def test_1994(self):
        assert "MCMXCIV" == intToRoman(1994)
