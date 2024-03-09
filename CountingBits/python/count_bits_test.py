from CountingBits.python.count_bits import countBits

class TestCountBits:
    def test_two(self):
        assert [0,1,1] == countBits(2)

    def test_five(self):
        assert [0,1,1,2,1,2] == countBits(5)
