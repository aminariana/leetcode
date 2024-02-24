import pytest
from DominoAndTrominoTiling.python import tiling

class TestTiling:
    def test_n1(self):
        assert 1 == tiling.numTilings(1)

    def test_n4(self):
        assert 11 == tiling.numTilings(4)

    def test_n5(self):
        assert 24 == tiling.numTilings(5)

    def test_n6(self):
        assert 53 == tiling.numTilings(6)

    def test_n10(self):
        assert 1255 == tiling.numTilings(10)

    def test_n1000(self):
        assert 979232805 == tiling.numTilings(1000)
