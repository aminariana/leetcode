from KidsWithCandies.python.kids_with_candies import kidsWithCandies

class TestKidsWithCandies:
    def test_one_loser(self):
        assert [True, True, True, False, True] == kidsWithCandies([2, 3, 5, 1, 3], 3)

    def test_one_winner(self):
        assert [True, False, False, False, False] == kidsWithCandies([4, 2, 1, 1, 2],  1)

    def test_almost_everyone(self):
        assert [True, False, True] == kidsWithCandies([12, 1, 12],  10)
