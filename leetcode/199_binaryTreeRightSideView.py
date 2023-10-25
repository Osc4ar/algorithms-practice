# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_view = []
        next_nodes = []
        level = 0

        if root:
            next_nodes.append(root)

        while len(next_nodes) > 0:
            for nodes_to_visit in range(len(next_nodes)):
                node = next_nodes.pop(0)

                # We only add the first element visited per level
                if len(right_side_view) == level:
                    right_side_view.append(node.val)

                if node.right:
                    next_nodes.append(node.right)
                if node.left:
                    next_nodes.append(node.left)

            level += 1

        return right_side_view