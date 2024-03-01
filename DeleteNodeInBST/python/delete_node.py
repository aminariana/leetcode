from typing import Optional

from Common.python.TreeNode import TreeNode


def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    # no tree
    if not root:
        return None
    # root is deleting
    if root.val == key:
        # promote the smallest right number
        if root.right:
            prev, min_right = None, root.right
            while min_right.left:
                prev, min_right = min_right, min_right.left
            # promote and delete
            root.val = min_right.val
            if prev:
                prev.left = min_right.right
            else:
                root.right = min_right.right
        # promote the largest left number
        elif root.left:
            prev, max_left = None, root.left
            while max_left.right:
                prev, max_left = max_left, max_left.right
            # promote and delete
            root.val = max_left.val
            if prev:
                prev.right = max_left.left
            else:
                root.left = max_left.left
        # stump, delete root and return nothing
        else:
            return None
    # root wasn't a match
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else: # if key < root.val:
        root.left = deleteNode(root.left, key)
    return root
