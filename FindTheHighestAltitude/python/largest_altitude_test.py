from FindTheHighestAltitude.python.largest_altitude import largestAltitude

class TestLargestAltitude:
    def test_dip(self):
        assert 1 == largestAltitude([-5,1,5,0,-7])

    def test_valley(self):
        assert 0 == largestAltitude([-4,-3,-2,-1,4,3,2])
