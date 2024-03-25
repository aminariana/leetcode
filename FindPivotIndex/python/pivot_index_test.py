from FindPivotIndex.python.pivot_index import pivotIndex

class TestPivotIndex:
    def test_has_pivot(self):
        assert 3 == pivotIndex([1,7,3,6,5,6])

    def test_no_pivot(self):
        assert -1 == pivotIndex([1,2,3])

    def test_start_pivot(self):
        assert 0 == pivotIndex([2,1,-1])

    def test_end_pivot(self):
        assert 2 == pivotIndex([-1,1,2])
