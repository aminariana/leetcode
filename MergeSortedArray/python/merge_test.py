from MergeSortedArray.python.merge import merge


class TestMerge:
    def test_normal(self):
        left = [1,2,3,0,0,0]
        right = [2,5,6]
        merge(left, 3, right, 3)
        assert left == [1,2,2,3,5,6]

    def test_noop(self):
        left = [1]
        right = []
        merge(left, 1, right, 0)
        assert left == [1]

    def test_copy(self):
        left = [0]
        right = [1]
        merge(left, 0, right, 1)
        assert left == [1]

    def test_shift(self):
        left = [4,5,6,0,0,0]
        right = [1,2,3]
        merge(left, 3, right, 3)
        assert left == [1,2,3,4,5,6]
