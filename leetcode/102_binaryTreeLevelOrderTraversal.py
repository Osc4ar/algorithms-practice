# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pending_nodes = [] # a queue
        level_order = []

        if root:
            pending_nodes.append(root)

        while len(pending_nodes) > 0:
            current_level = []

            for nodes_to_delete in range(len(pending_nodes)):
                node = pending_nodes.pop(0) # we pop first element to behave as a queue
                current_level.append(node.val)

                if node.left:
                    pending_nodes.append(node.left)
                if node.right:
                    pending_nodes.append(node.right)

            level_order.append(current_level)

        return level_order
        