from KthLargestElementInAnArray.python.find_kth_largest import findKthLargest_optimal

class TestFindKthLargest:
    def test_works(self):
        assert 5 == findKthLargest_optimal([3,2,1,5,6,4], 2)

    def test_handles_dups(self):
        assert 4 == findKthLargest_optimal([3,2,3,1,2,4,5,5,6], 4)
