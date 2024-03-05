from Common.python.TreeNode import TreeNode


def goodNodes(root: TreeNode) -> int:
    stack = [(root, root.val)]
    good = 0
    while len(stack):
        (current, best) = stack.pop()
        if current.val >= best:
            good += 1
            best = current.val
        if current.left: stack.append((current.left, best))
        if current.right: stack.append((current.right, best))
    return good
