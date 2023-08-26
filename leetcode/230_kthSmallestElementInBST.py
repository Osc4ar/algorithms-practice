# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_nums = self.get_inorder_nums(root)

        return inorder_nkums[k-1]

    def get_inorder_nums(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        inorder_nodes = []

        inorder_nodes += self.get_inorder_nums(root.left)
        inorder_nodes += [root.val]
        inorder_nodes += self.get_inorder_nums(root.right)

        return inorder_nodes