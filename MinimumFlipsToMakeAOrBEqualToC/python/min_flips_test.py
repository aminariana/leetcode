from MinimumFlipsToMakeAOrBEqualToC.python.min_flips import minFlips

class TestMinFlips:
    def test_265(self):
        assert 3 == minFlips(2, 6, 5)

    def test_427(self):
        assert 1 == minFlips(4, 2, 7)

    def test_123(self):
        assert 0 == minFlips(1, 2, 3)
