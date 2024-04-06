from RottingOranges.python.rotting_oranges import orangesRotting

class TestOrangesRotting:
    def test_rot_in_4_minutes(self):
        assert 4 == orangesRotting([
            [2,1,1],
            [1,1,0],
            [0,1,1]])

    def test_immune(self):
        assert -1 == orangesRotting([
            [2,1,1],
            [0,1,1],
            [1,0,1]])

    def test_already_rotten(self):
        assert 0 == orangesRotting([[0,2]])

    def test_too_far(self):
        assert -1 == orangesRotting([[0,1,0,2]])
