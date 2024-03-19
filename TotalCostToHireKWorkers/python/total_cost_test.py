from TotalCostToHireKWorkers.python.total_cost import totalCost

class TestTotalCost:
    def test_basic_unique(self):
        assert 11 == totalCost([17,12,10,2,7,2,11,20,8], 3, 4)

    def test_tie_and_overlap(self):
        assert 4 == totalCost([1,2,4,1], 3, 3)

    def test_single(self):
        assert 1 == totalCost([1], 1, 1)

    def test_complex_example(self):
        assert 423 == totalCost([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], 11, 2)

    def test_complex_long_example(self):
        assert 223 == totalCost([18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75], 13, 23)

    def test_ties(self):
        assert 3000 == totalCost([1] * 3000, 3000, 1500)
