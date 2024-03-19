from MaximumSubsequenceScore.python.max_score import maxScore

class TestMaxScore:
    def test_basic(self):
        assert 12 == maxScore([1,3,3,2], [2,1,3,4], 3)

    def test_long(self):
        assert 30 == maxScore([4,2,3,1,1], [7,5,10,9,6], 1)

    def test_trick(self):
        assert 168 == maxScore([2,1,14,12], [11,7,13,6], 3)
