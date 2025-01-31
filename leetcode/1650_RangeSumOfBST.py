# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    1. Iterate the three with DFS
    2. Check if the node is on the range
    3. If it is on the range, return the value plus the sum of the left and right
    4. If not, just return the sum of the left and right children
    5. If the value is smaller than low, we can skip the values of the left
    6. If the value is bigger than high, we can skip the values on the right
    '''
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        result = 0
        if root.val >= low:
            result += self.rangeSumBST(root.left, low, high)
        if root.val <= high:
            result += self.rangeSumBST(root.right, low, high)
        if root.val >= low and root.val <= high:
            result += root.val

        return result
