from Common.python.TreeNode import TreeNode


def lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root in [p, q]:
        return root
    else:
        left, right = lca(root.left, p, q), lca(root.right, p, q)
        return root if left and right else left or right
