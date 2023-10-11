# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        newTargetSum = targetSum - root.val

        if newTargetSum == 0 and root.left is None and root.right is None:
            return True
        if self.hasPathSum(root.left, newTargetSum):
            return True
        if self.hasPathSum(root.right, newTargetSum):
            return True

        return False