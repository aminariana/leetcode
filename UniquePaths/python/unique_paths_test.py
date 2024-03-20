from UniquePaths.python.unique_paths import uniquePaths

class TestUniquePaths:
    def test_one_by_one(self):
        assert 1 == uniquePaths(1, 1)

    def test_wide(self):
        assert 28 == uniquePaths(3, 7)

    def test_tall(self):
        assert 3 == uniquePaths(3, 2)
