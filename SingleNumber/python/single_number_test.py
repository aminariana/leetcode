from SingleNumber.python.single_number import singleNumber

class TestSingleNumber:
    def test_no_dup(self):
        assert 1 == singleNumber([1])

    def test_one_dup(self):
        assert 1 == singleNumber([2,2,1])

    def test_two_dup(self):
        assert 4 == singleNumber([4,1,2,1,2])
