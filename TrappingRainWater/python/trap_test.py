from TrappingRainWater.python.trap import trap

class TestTrap:
    def test_empty(self):
        assert 0 == trap([])

    def test_hill(self):
        assert 0 == trap([0, 1, 2, 1, 0])

    def test_bowl(self):
        assert 4 == trap([2, 1, 0, 1, 2])

    def test_normal(self):
        assert 6 == trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
