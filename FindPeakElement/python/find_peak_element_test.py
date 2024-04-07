from FindPeakElement.python.find_peak_element import findPeakElement

class TestFindPeakElement:
    def test_one_peak(self):
        assert 2 == findPeakElement([1,2,3,1])

    def test_two_peaks(self):
        assert 5 == findPeakElement([1,2,1,3,5,6,4])

    def test_edge_peak(self):
        assert 0 == findPeakElement([2,1])
