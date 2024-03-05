from Common.python.TreeNode import tree_from_list
from CountGoodNodesInBinaryTree.python.good_nodes import goodNodes

class TestGoodNodes:
    def test_root(self):
        assert 1 == goodNodes(tree_from_list([1]))

    def test_equal_child(self):
        assert 2 == goodNodes(tree_from_list([1, 1]))

    def test_greater_child(self):
        assert 2 == goodNodes(tree_from_list([1, 2]))

    def test_lesser_child(self):
        assert 1 == goodNodes(tree_from_list([1, 0]))

    def test_balanced_good_and_bad(self):
        assert 4 == goodNodes(tree_from_list([3,1,4,3,None,1,5]))

    def test_deep_good_and_bad(self):
        assert 3 == goodNodes(tree_from_list([3,3,None,4,2]))
