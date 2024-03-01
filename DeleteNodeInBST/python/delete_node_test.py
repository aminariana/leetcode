from Common.python.TreeNode import TreeNode, tree_from_list, tree_to_list
from DeleteNodeInBST.python.delete_node import deleteNode

class TestDeleteNode:
    def test_delete_from_empty(self):
        assert [] == tree_to_list(deleteNode(tree_from_list([]), 0))

    def test_miss_single(self):
        assert [5] == tree_to_list(deleteNode(tree_from_list([5]), 1))

    def test_hit_single(self):
        assert [] == tree_to_list(deleteNode(tree_from_list([5]), 5))

    def test_miss_big_tree(self):
        assert [5,3,6,2,4,None,7] == tree_to_list(deleteNode(tree_from_list([5,3,6,2,4,None,7]), 0))

    def test_hit_big_tree(self):
        assert [5,4,6,2,None,None,7] == tree_to_list(deleteNode(tree_from_list([5,3,6,2,4,None,7]), 3))
