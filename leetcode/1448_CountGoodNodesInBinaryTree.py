# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    1. Iterate the tree using DFS, on every call send a min_value we have to check
    2. If the current node is greater or equal to the min_value, increase our count by 1
    3. Call the recursive function with a new min_value, which will be the maximun between
        min_value and current value
    4. This solution requires to visit every Node on the tree
    '''
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node: TreeNode, min_value):
            if node is None:
                return

            new_min = min_value
            if node.val >= min_value:
                new_min = node.val
                self.count += 1

            dfs(node.left, new_min)
            dfs(node.right, new_min)

        dfs(root, float('-inf'))
        return self.count
