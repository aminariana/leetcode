from CanPlaceFlowers.python.can_place_flowers import canPlaceFlowers

class TestCanPlaceFlowers:
    def test_one_in_the_middle(self):
        assert canPlaceFlowers([1,0,0,0,1], 1)

    def test_two_not_fit_the_middle(self):
        assert not canPlaceFlowers([1,0,0,0,1], 2)

    def test_two_not_fit_together_in_the_middle(self):
        assert not canPlaceFlowers([1,0,0,0,0,1], 2)
