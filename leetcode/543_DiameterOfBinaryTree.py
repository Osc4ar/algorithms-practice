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

        
        self.maxDiameter = 0
        def depthOfTree(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            
            leftDepth = depthOfTree(root.left)
            rightDepth = depthOfTree(root.right)
            diameter = leftDepth + rightDepth
            self.maxDiameter = max(self.maxDiameter, diameter)

            return 1 + max(leftDepth, rightDepth)

        depthOfTree(root)
        return self.maxDiameter
