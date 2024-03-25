from Common.python.TreeNode import tree_from_list
from LongestZigZagPathInABinaryTree.python.longest_zigzag import longestZigZag

class TestLongestZigZag:
    def test_root(self):
        assert 0 == longestZigZag(root=tree_from_list([1]))

    def test_righty(self):
        assert 1 == longestZigZag(root=tree_from_list([1,None,1]))

    def test_lefty(self):
        assert 1 == longestZigZag(root=tree_from_list([1,1,None]))

    def test_left_zigzag(self):
        assert 2 == longestZigZag(root=tree_from_list([1,1,None,None,1]))

    def test_mid_tree_left_zigzag(self):
        assert 2 == longestZigZag(root=tree_from_list([1,1,None,1,None,None,1]))

    def test_right_long(self):
        assert 3 == longestZigZag(root=tree_from_list([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1]))

    def test_mid_tree_four_long(self):
        assert 4 == longestZigZag(root=tree_from_list([1,1,1,None,1,None,None,1,1,None,1]))
