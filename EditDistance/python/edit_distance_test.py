from EditDistance.python.edit_distance import Solution

class TestEditDistance:
    def test_horse_ros(self):
        assert 3 == Solution().minDistance_2D_DP("horse", "ros")
        assert 3 == Solution().minDistance_1D_DP("horse", "ros")

    def test_intention_execution(self):
        assert 5 == Solution().minDistance_2D_DP("intention", "execution")
        assert 5 == Solution().minDistance_1D_DP("intention", "execution")

    def test_empty_string_ros(self):
        assert 3 == Solution().minDistance_2D_DP("", "ros")
        assert 3 == Solution().minDistance_1D_DP("", "ros")

    def test_babak_kabab(self):
        assert 2 == Solution().minDistance_2D_DP("babak", "kabab")
        assert 2 == Solution().minDistance_1D_DP("babak", "kabab")

    def test_howmuchwood(self):
        assert 15 == Solution().minDistance_2D_DP("howmuchwoodwouldawoodchuckchuckifawoodchuckcouldchuckwood", "noamountofwoodwouldawoodchuckchucksinceawoodchuckcantchuckwood")
        assert 15 == Solution().minDistance_1D_DP("howmuchwoodwouldawoodchuckchuckifawoodchuckcouldchuckwood", "noamountofwoodwouldawoodchuckchucksinceawoodchuckcantchuckwood")
