"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def find_path(root: 'Node', path):
            path.append(root)

            if root.parent is None:
                return

            find_path(root.parent, path)

        p_path = []
        q_path = []
        find_path(p, p_path)
        find_path(q, q_path)

        p_path = p_path[::-1]
        q_path = q_path[::-1]

        shortest = min(len(p_path), len(q_path))
        for i in range(shortest):
            if p_path[i].val != q_path[i].val:
                return p_path[i-1]
        
        return p_path[shortest-1]
