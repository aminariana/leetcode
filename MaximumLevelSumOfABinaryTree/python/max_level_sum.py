from typing import Optional

from Common.python.TreeNode import TreeNode


def maxLevelSum(root: Optional[TreeNode]) -> int:
    current_level, current_sum = 1, root.val if root else 0
    max_level, max_sum = current_level, current_sum
    q_current, q_next = [root], []
    while len(q_current) or len(q_next):
        node = q_current.pop()
        current_sum += node.val
        if node.left: q_next.append(node.left)
        if node.right: q_next.append(node.right)
        # once level is seen
        if not len(q_current):
            if current_sum > max_sum:
                max_sum = current_sum
                max_level = current_level
            q_current, q_next = q_next, q_current
            current_level += 1
            current_sum = 0
    return max_level
    