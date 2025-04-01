# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    1. Iterate the tree using DFS to follow a single path each time
    2. Keep a max variable, which contains the biggest value in the path
    3. If the current node is greater than or equal to the max value, increase the count of good nodes by 1
    4. Return the count at the end
    '''
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def dfs(node: Optional[TreeNode], max_val: int):
            if node is None:
                return

            new_max = max_val
            if node.val >= max_val:
                self.good += 1
                new_max = node.val

            dfs(node.left, new_max)
            dfs(node.right, new_max)

        dfs(root, float('-inf'))
        return self.good
