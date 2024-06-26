from SearchInABinarySearchTree.python.search_bst import searchBST_iterative, searchBST_recursive
from Common.python.TreeNode import tree_to_list, tree_from_list

class TestSearchBst:
    def test_find_recursive(self):
        result_node = searchBST_recursive(tree_from_list([4,2,7,1,3]), 2)
        assert [2,1,3] == tree_to_list(result_node)

    def test_find_iterative(self):
        result_node = searchBST_recursive(tree_from_list([4,2,7,1,3]), 2)
        assert [2,1,3] == tree_to_list(result_node)

    def test_not_find_recursive(self):
        result_node = searchBST_recursive(tree_from_list([4,2,7,1,3]), 5)
        assert [] == tree_to_list(result_node)

    def test_not_find_iterative(self):
        result_node = searchBST_iterative(tree_from_list([4,2,7,1,3]), 5)
        assert [] == tree_to_list(result_node)
