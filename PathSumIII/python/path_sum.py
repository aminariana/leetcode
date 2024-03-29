from collections import defaultdict
from typing import Optional

from Common.python.TreeNode import TreeNode

def pathSum_recursive_optimized(root: Optional[TreeNode], targetSum: int) -> int:
    # definition: a prefix is the sum of a path from *ROOT* to NODE.
    # the insight here is that this is a sliding window problem on tree.
    prefixes = defaultdict(int)
    # a sum of zero from the root has only one corresponding prefix (the empty set)
    prefixes[0] = 1
    def dfs(node: Optional[TreeNode], prefix: int) -> int:
        if not node: return 0
        prefix += node.val
        overshoot = prefix - targetSum
        # corrections are prior shorter prefixes that can be cut from this one to make a non-rooted target sum 
        corrections = prefixes[overshoot]
        # keep track of prefix counts
        prefixes[prefix] += 1
        res = corrections + dfs(node.left, prefix) + dfs(node.right, prefix)
        # once this node-subtree is done, don't track its prefix as we go back up the recursive stack
        prefixes[prefix] -= 1
        if prefixes[prefix] == 0: del prefixes[prefix]
        return res
    
    return dfs(root, 0)

def pathSum_recursive(root: Optional[TreeNode], targetSum: int) -> int:
    def dfs(node: Optional[TreeNode], runningSum: int = 0, running: bool = False) -> int:
        if not node:
            return 0

        result = 0
        if not running:
            result += dfs(node.left, 0) + dfs(node.right, 0)
        runningSum += node.val
        if runningSum == targetSum:
            result += 1
        result += dfs(node.left, runningSum, True) + dfs(node.right, runningSum, True)
        return result
    return dfs(root)


def pathSum_iterative(root: Optional[TreeNode], targetSum: int) -> int:
    count = 0
    stack = []
    if root:
        stack.append((root, 0, True))
    while len(stack):
        # can_restart_path prevents double counting valid subpaths by two ancestors
        # e.g. the leaf in 1->2->3 (target 3) by both 1 and 2 starts.
        (current, prefix_val, can_restart_path) = stack.pop()
        if prefix_val + current.val == targetSum:
            count += 1
        prefix_val += current.val
        if left := current.left:
            stack.append((left, prefix_val, False))
            if can_restart_path:
                stack.append((left, 0, True))
        if right := current.right:
            stack.append((right, prefix_val, False))
            if can_restart_path:
                stack.append((right, 0, True))
    return count