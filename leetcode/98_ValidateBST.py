# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], min_value, max_value) -> bool:
            if root is None:
                return True

            if root.val <= min_value or root.val >= max_value:
                return False
            
            if (root.left and root.val <= root.left.val) or (root.right and root.val >= root.right.val):
                return False
    
            return dfs(root.left, min_value, min(max_value, root.val)) and dfs(root.right, max(min_value, root.val), max_value)

        return dfs(root, float('-inf'), float('inf'))
