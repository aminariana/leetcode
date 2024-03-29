from Common.python.TreeNode import tree_from_list
from PathSumIII.python.path_sum import pathSum_recursive_optimized as pathSum

class TestPathSum:
    def test_avg(self):
        assert 3 == pathSum(tree_from_list([10,5,-3,3,2,None,11,3,-2,None,1]), 8)

    def test_long(self):
        assert 3 == pathSum(tree_from_list([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22)

    def test_righty(self):
        assert 2 == pathSum(tree_from_list([1,None,2,None,3,None,4,None,5]), 3)

    def test_sub_sum_zero(self):
        assert 2 == pathSum(tree_from_list([-8,6,8,None,None,8,2,None,None,None,-2]), -2)
