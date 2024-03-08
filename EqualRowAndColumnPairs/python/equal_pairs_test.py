from EqualRowAndColumnPairs.python.equal_pairs import equalPairs

class TestEqualPairs:
    def test_mid_col_end_row(self):
        assert 1 == equalPairs([
            [3,2,1],
            [1,7,6],
            [2,7,7]])

    def test_multi_match(self):
        assert 3 == equalPairs([
            [3,1,2,2],
            [1,4,4,5],
            [2,4,2,2],
            [2,4,2,2]])

    def test_huge_hash(self):
        assert 0 == equalPairs([list(range(200))] * 200)

