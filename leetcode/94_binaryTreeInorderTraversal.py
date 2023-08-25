# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        inorder_nodes = []

        inorder_nodes += self.inorderTraversal(root.left)
        inorder_nodes += [root.val]
        inorder_nodes += self.inorderTraversal(root.right)

        return inorder_nodes
