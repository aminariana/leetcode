from typing import List, Optional

from Common.python.TreeNode import TreeNode


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    def dfs(root: Optional[TreeNode], root_depth: int = 0, result_depth: int = 0):
        if root:
            if root_depth == result_depth:
                yield root
                result_depth += 1
            for right_node in dfs(root.right, root_depth + 1, result_depth):
                yield right_node
                result_depth += 1
            for left_node in dfs(root.left, root_depth + 1, result_depth):
                yield left_node
                result_depth += 1
    return [node.val for node in dfs(root)]
