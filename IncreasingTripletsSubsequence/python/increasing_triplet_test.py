from IncreasingTripletsSubsequence.python.increasing_triplet import increasingTriplet

class TestIncreasingTriplet:
    def test_range(self):
        assert increasingTriplet([1,2,3,4,5])

    def test_reversed_range(self):
        assert not increasingTriplet([5,4,3,2,1])

    def test_triplet_after_noise(self):
        assert increasingTriplet([2,1,5,0,4,6])

    def test_noise_after_triplet(self):
        assert increasingTriplet([4,5,2147483647,1,2])

    def test_anomaly_between_triplet(self):
        assert increasingTriplet([1,2,1,3])
