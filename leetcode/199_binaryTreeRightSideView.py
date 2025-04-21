# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Use BFS in the tree, add to the result the last value visited in each level
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        result = []

        while queue:
            last_value = None
            for _ in range(len(queue)):
                node = queue.popleft()
                last_value = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(last_value)

        return result
