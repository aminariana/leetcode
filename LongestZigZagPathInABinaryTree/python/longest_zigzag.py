from typing import Optional

from Common.python.TreeNode import TreeNode


def longestZigZag(root: Optional[TreeNode]) -> int:
    stack = [(root, 0, None)]
    best = 0
    while len(stack):
        (current, value, isCurrentLeftChild) = stack.pop()
        if current.left:
            new_value = value + 1 if isCurrentLeftChild != True else 1
            stack.append((current.left, new_value, True))
        if current.right:
            new_value = value + 1 if isCurrentLeftChild != False else 1
            stack.append((current.right, new_value, False))
        best = max(best, value)
    return best




