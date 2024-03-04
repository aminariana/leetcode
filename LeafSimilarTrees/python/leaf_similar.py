from itertools import zip_longest
from typing import Optional

from Common.python.TreeNode import TreeNode


def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def dfs_leaf_enumerator(root: Optional[TreeNode]):
        if root:
            for leaf in dfs_leaf_enumerator(root.left): yield leaf
            if not root.left and not root.right: yield root.val
            for leaf in dfs_leaf_enumerator(root.right): yield leaf


    for (n1, n2) in zip_longest(dfs_leaf_enumerator(root1), dfs_leaf_enumerator(root2)):
        if n1 != n2: return False
    return True
