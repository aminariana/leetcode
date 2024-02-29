from typing import Optional

from Common.python.TreeNode import TreeNode


def searchBST_iterative(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    while root:
        if root.val < val: root = root.right
        elif root.val > val: root = root.left
        else: return root
    else: return None

def searchBST_recursive(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root == None or root.val == val:
        return root
    elif root.val < val:
        return searchBST_recursive(root.right, val)
    else:
        return searchBST_recursive(root.left, val)