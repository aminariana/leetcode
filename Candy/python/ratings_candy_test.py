from Candy.python.ratings_candy import Solution


class TestCandy:
    def test_hill(self):
        assert 21 == Solution().candy([1,2,3,5,4,3,2,1])
        assert 21 == Solution().candy_dfs([1,2,3,5,4,3,2,1])

    def test_short_changed_tie(self):
        assert 4 == Solution().candy([1,2,2])
        assert 4 == Solution().candy_dfs([1,2,2])

    def test_increasing(self):
        assert 10 == Solution().candy([10, 20, 30, 40])
        assert 10 == Solution().candy_dfs([10, 20, 30, 40])

    def test_decreasing(self):
        assert 10 == Solution().candy([40, 30, 20, 10])
        assert 10 == Solution().candy_dfs([40, 30, 20, 10])

    def test_valley(self):
        assert 12 == Solution().candy([40, 30, 20, 10, 20])
        assert 12 == Solution().candy_dfs([40, 30, 20, 10, 20])

    def test_plateau(self):
        assert 13 == Solution().candy([1,2,87,87,87,2,1])
        assert 13 == Solution().candy_dfs([1,2,87,87,87,2,1])

    def test_retrospective_hill(self):
        assert 24 == Solution().candy([10,20,30,29,28,27,26,25])
        assert 24 == Solution().candy_dfs([10,20,30,29,28,27,26,25])

    def test_revised_peak(self):
        assert 21 == Solution().candy([1,2,3,5,4,3,2,1])
        assert 21 == Solution().candy_dfs([1,2,3,5,4,3,2,1])
