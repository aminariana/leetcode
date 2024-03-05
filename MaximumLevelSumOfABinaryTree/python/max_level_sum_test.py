from Common.python.TreeNode import tree_from_list
from MaximumLevelSumOfABinaryTree.python.max_level_sum import maxLevelSum

class TestMaxLevelSum:
    def test_maximizes_positives(self):
        assert 2 == maxLevelSum(tree_from_list([1,7,0,7,-8,None,None]))

    def test_maximizes_sum_not_element(self):
        assert 2 == maxLevelSum(tree_from_list([989,None,10250,98693,-89388,None,None,None,-32127]))

    def test_maximizes_negative_sums(self):
        assert 3 == maxLevelSum(tree_from_list([-100,-200,-300,-20,-5,-10,None]))

    def test_breaks_a_tie_by_first_sum_not_tricked_by_partial_sums(self):
        assert 1 == maxLevelSum(tree_from_list([1,1,0,7,-8,-7,9]))
