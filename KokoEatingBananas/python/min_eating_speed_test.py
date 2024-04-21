from KokoEatingBananas.python.min_eating_speed import minEatingSpeed

class TestMinEatingSpeed:
    def test_some_two_efforts(self):
        assert 4 == minEatingSpeed([3,6,7,11], 8)

    def test_discrete_time_boxes(self):
        assert 30 == minEatingSpeed([30,11,23,4,20], 5)

    def test_inefficient_time_boxes(self):
        assert 23 == minEatingSpeed([30,11,23,4,20], 6)

    def test_almost_one_bite(self):
        assert 2 == minEatingSpeed([312884470], 312884469)
