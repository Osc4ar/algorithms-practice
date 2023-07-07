# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key == root.val:
            # Single leaf scenario
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # Two leafs scenario using smallest value in the right
            min_child = self.minChild(root.right)
            root.val = min_child.val
            root.right = self.deleteNode(root.right, min_child.val)
            return root



        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root

    def minChild(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current_node = root

        while current_node and current_node.left:
            current_node = current_node.left

        return current_node