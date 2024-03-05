from BinaryTreeRightSideView.python.right_side_view import rightSideView
from Common.python.TreeNode import tree_from_list

class TestRightSideView:
    def test_empty(self):
        assert [] == rightSideView(tree_from_list([]))

    def test_righty(self):
        assert [1,3] == rightSideView(tree_from_list([1,None,3]))

    def test_balanced(self):
        assert [1,3,4] == rightSideView(tree_from_list([1,2,3,None,5,None,4]))

    def test_lefty(self):
        assert [1,3,5] == rightSideView(tree_from_list([1,2,3,None,5,None]))
