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
            if pop:
                list.append(pop.val)
                if pop.left or pop.right:
                    q.append(pop.left)            
                    q.append(pop.right)
            else:
                list.append(None)
    return list

def tree_from_list(list: List[int]) -> TreeNode:
    if not list:
        return None
    if not len(list):
        return list
    root = TreeNode(list[0]) if list[0] != None else None
    q = deque([root])
    i = 1
    while i < len(list) and len(q):
        if current := q.popleft():
            if i < len(list):
                current.left = TreeNode(list[i]) if list[i] != None else None
                i += 1
            if i < len(list):
                current.right = TreeNode(list[i]) if list[i] != None else None
                i += 1
            if current.left or current.right:
                q.append(current.left)
                q.append(current.right)
    return root
