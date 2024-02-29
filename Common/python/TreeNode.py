# Definition for a binary tree node.
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_list(root: TreeNode) -> List[int]:
    list = []
    if root:
        q = deque([root])
        while len(q):
            pop = q.popleft()
            list.append(pop.val)
            if pop.left:
                q.append(pop.left)            
            if pop.right:
                q.append(pop.right)
    return list

def tree_from_list(list: List[int]) -> TreeNode:
    if not list:
        return None
    root = None
    q = deque()
    for val in list:
        valNode = TreeNode(val) if val else None
        if len(q):
            current = q[0]
            if not current.left:
                current.left = valNode
            elif not current.right:
                current.right = valNode
                q.popleft() # current is filled up and done
        if valNode:    
            q.append(valNode)
        if not root:
            root = valNode
    return root
