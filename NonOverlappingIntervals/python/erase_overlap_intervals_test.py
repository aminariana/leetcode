from NonOverlappingIntervals.python.erase_overlap_intervals import eraseOverlapIntervals

class TestEraseOverlapIntervals:
    def test_one(self):
        assert 1 == eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])

    def test_dups(self):
        assert 2 == eraseOverlapIntervals([[1,2],[1,2],[1,2]])

    def test_none(self):
        assert 0 == eraseOverlapIntervals([[1,2],[2,3]])

    def test_negative(self):
        assert 1 == eraseOverlapIntervals([[-2, -1],[-3, -2],[-4, -3],[-3, -1]])
