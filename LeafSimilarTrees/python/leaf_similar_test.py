from Common.python.TreeNode import tree_from_list
from LeafSimilarTrees.python.leaf_similar import leafSimilar

class TestLeafSimilar:
    def test_different_small_shapes_are_leaf_similar(self):
        assert leafSimilar(
            tree_from_list([1,2,3,4]),
            tree_from_list([1,4,2,None,None,3]))

    def test_different_big_shapes_are_leaf_similar(self):
        assert leafSimilar(
            tree_from_list([3,5,1,6,2,9,8,None,None,7,4]),
            tree_from_list([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]))

    def test_same_small_shapes_and_same_leaf_sets_can_be_dissimilar(self):
        assert not leafSimilar(
            tree_from_list([1,2,3]),
            tree_from_list([1,3,2]))
