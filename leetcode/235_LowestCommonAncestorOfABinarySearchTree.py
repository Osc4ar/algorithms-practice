# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Use DFS to list all the ancestors of a given Node (p or q)
Once we have the two lists, find the common ancestor between them by comparing both lists,
the common ancestor is the last element which is the same in both lists
p = 0, [6,2,0]
q = 3, [6,2,4,3]

Time Complexity: In the worst case scenario we will iterate all the nodes of the tree for each Node, then we have a time complexity of O(2*n) or O(n) to simplify
Space complexity: In the worst case scenario we will store all the nodes of the tree in two arrays, therefore we will have O(n)
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pPath = self.path(root, p, [])
        qPath = self.path(root, q, [])

        min_len = min(len(pPath), len(qPath))
        for i in range(min_len):
            if pPath[i] != qPath[i]:
                return pPath[i-1]

        return pPath[min_len-1]

    def path(self, root: 'TreeNode', target: 'TreeNode', path: list['TreeNode']) -> list['TreeNode']:
        if root is None:
            return []
        
        path.append(root)

        if root.val == target.val:
            return path[:]

        leftPath = self.path(root.left, target, path)
        rightPath = self.path(root.right, target, path)

        path.pop()

        if len(leftPath) > 0:
            return leftPath
        else:
            return rightPath
