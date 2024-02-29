from Common.python.TreeNode import TreeNode, tree_from_list, tree_to_list


class TestTreeNode:
    def test_value(self):
        root = TreeNode(1)
        assert 1 == root.val
        
    def test_nesting(self):
        left = TreeNode(2)
        right = TreeNode(3)
        root = TreeNode(1, left, right)
        assert 1 == root.val
        assert 2 == root.left.val
        assert 3 == root.right.val

    def test_from_list_of_single(self):
        root = tree_from_list([1])
        assert 1 == root.val
        assert [1] == tree_to_list(root)

    def test_from_list_of_none(self):
        root = tree_from_list([None])
        assert None == root
        assert [] == tree_to_list(root)

    def test_from_list(self):
        root = tree_from_list([1, 2, 3])
        assert 1 == root.val
        assert 2 == root.left.val
        assert 3 == root.right.val
        assert [1, 2, 3] == tree_to_list(root)

    def test_from_deep_list(self):
        root = tree_from_list([1, 2, 3, 4, 5, 6, 7])
        assert 1 == root.val
        assert 2 == root.left.val
        assert 3 == root.right.val
        assert 4 == root.left.left.val
        assert 5 == root.left.right.val
        assert 6 == root.right.left.val
        assert 7 == root.right.right.val
        assert [1, 2, 3, 4, 5, 6, 7] == tree_to_list(root)
