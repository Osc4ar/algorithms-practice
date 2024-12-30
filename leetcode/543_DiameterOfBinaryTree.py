# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Because it is a binary tree, we could say the diameter is the longest path of the left plus
the longest path of the right side of the tree.
So we can find the diameter of the tree by adding the longest paths of each of the children of a node
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        currentDepth = self.depthOfTree(root.left) + self.depthOfTree(root.right)
        diameterOfLeft = self.diameterOfBinaryTree(root.left)
        diameterOfRight = self.diameterOfBinaryTree(root.right)
        return max(currentDepth, diameterOfLeft, diameterOfRight)


    def depthOfTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.depthOfTree(root.left), self.depthOfTree(root.right))
        
