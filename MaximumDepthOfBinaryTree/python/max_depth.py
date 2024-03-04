from typing import Optional

from Common.python.TreeNode import TreeNode

def maxDepth(root: Optional[TreeNode]) -> int:
    return 1 + max(maxDepth(root.left), maxDepth(root.right)) if root else 0
