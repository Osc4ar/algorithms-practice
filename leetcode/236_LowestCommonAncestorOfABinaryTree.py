# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    1. Find the node p on the tree, save its path on a list
    2. Find the node q on the tree, save its path on a list
    3. Compare both paths, as soon as one of the list is different from the other return the previous value
    4. If one list ends before that condition, return the last element of the shorter list
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = []
        self.get_path(root, p, path_p)
        path_q = []
        self.get_path(root, q, path_q)

        shortest_path = min(len(path_p), len(path_q))
        for i in range(shortest_path):
            if path_p[i].val != path_q[i].val:
                return path_p[i - 1]

        return path_p[shortest_path - 1]

    def get_path(self, root: 'TreeNode', target: 'TreeNode', path: list[int]) -> bool:
        if root is None:
            return False

        if root.val == target.val:
            path.append(root)
            return True

        path.append(root)
        left = self.get_path(root.left, target, path)
        right = self.get_path(root.right, target, path)

        if left or right:
            return True

        path.pop()
        return False
