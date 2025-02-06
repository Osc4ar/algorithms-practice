# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    We can use DFS with Backtracking as follows:
    1. Check if the node is a leaf, if it is not add it to the path and visit its children
    2. If the node is a leaf, conver its path to the integer it represents and add it to the a list of paths
    3. Once we have a list of every path, sum all of them
    '''
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        paths = []

        def dfs(root: Optional[TreeNode], path):
            if root is None:
                return
            
            path.append(root.val)
            if root.left is None and root.right is None:
                res = 0
                for i, n in enumerate(reversed(path)):
                    res += n * 10**i
                paths.append(res)
            else:
                dfs(root.left, path)
                dfs(root.right, path)
            path.pop()

        dfs(root, [])
        return sum(paths)
