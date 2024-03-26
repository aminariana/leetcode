from Common.python.TreeNode import tree_from_list
from LowestCommonAncestorOfABinaryTree.python.lca import lca

class TestLCA:
    def test_root_of_large_tree(self):
        root = tree_from_list([3,5,1,6,2,0,8,None,None,7,4])
        assert root == lca(root, root.left, root.right)

    def test_middle_of_large_tree(self):
        root = tree_from_list([3,5,1,6,2,0,8,None,None,7,4])
        assert root.left == lca(root, root.left.right.right, root.left)

    def test_root_of_lefty(self):
        root = tree_from_list([1,2])
        assert root == lca(root, root, root.left)

    def test_root_of_balanced(self):
        root = tree_from_list([1,2,3])
        assert root == lca(root, root.left, root.right)

    def test_root_of_lefty_long(self):
        root = tree_from_list([1,2,None,3])
        assert root.left == lca(root, root.left, root.left.left)
