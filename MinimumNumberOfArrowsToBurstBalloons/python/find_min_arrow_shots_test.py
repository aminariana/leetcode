from MinimumNumberOfArrowsToBurstBalloons.python.find_min_arrow_shots import findMinArrowShots

class TestFindMinArrowShots:
    def test_four_balloons_two_arrows(self):
        assert 2 == findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])

    def test_four_balloons_four_arrows(self):
        assert 4 == findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])

    def test_four_just_touching_two_arrows(self):
        assert 2 == findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])
