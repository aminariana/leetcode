from Common.python.TreeNode import tree_from_list
from MaximumDepthOfBinaryTree.python.max_depth import maxDepth

class TestMaxDepth:
    def test_root(self):
        assert 1 == maxDepth(tree_from_list([1]))

    def test_two_on_right(self):
        assert 2 == maxDepth(tree_from_list([1,None,2]))

    def test_two_on_left(self):
        assert 2 == maxDepth(tree_from_list([1,2,None]))

    def test_two_on_both(self):
        assert 2 == maxDepth(tree_from_list([1,2,3]))

    def test_three_on_right(self):
        assert 3 == maxDepth(tree_from_list([3,9,20,None,None,15,7]))

    def test_three_on_left(self):
        assert 3 == maxDepth(tree_from_list([3,9,20,15,7,None,None]))
