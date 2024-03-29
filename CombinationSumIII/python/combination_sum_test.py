from CombinationSumIII.python.combination_sum import combinationSum3_dp as combinationSum3

class TestCombinationSum:
    def test_negative(self):
        assert [] == combinationSum3(4, 1)

    def test_three_numbers_totalling_seven(self):
        assert [[1,2,4]] == combinationSum3(3, 7)

    def test_three_numbers_totalling_nine(self):
        assert [[1,2,6],[1,3,5],[2,3,4]] == combinationSum3(3, 9)
