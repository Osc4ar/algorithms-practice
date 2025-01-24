# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    General ideal:
    Using BFS, traverse the tree and keep adding nodes to the result by keeping track of each node's column
    1. Use BFS to iterate the tree
    2. In the queue, save the Node with its potential column, the first element will have column 0
    3. If we have a left node, we will need to shift all the columns to the right one position, since we are introducing a new column to the left
    4. If we have a right node, we added it to the result on the rightmost position
    5. We iterate every node until the queue is empty
    '''
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = deque()
        result.append([root.val])
        queue = deque()
        queue.append((root, 0))

        while queue:
            offset = 0
            for _ in range(len(queue)):
                node, col = queue.popleft()
                if node.left:
                    new_col = col - 1 + offset
                    if new_col < 0:
                        result.appendleft([node.left.val])
                        offset += 1
                        new_col = 0
                    else:
                        result[new_col].append(node.left.val)
                    queue.append((node.left, new_col))
                if node.right:
                    new_col = col + 1 + offset
                    if new_col >= len(result):
                        result.append([node.right.val])
                    else:
                        result[new_col].append(node.right.val)
                    queue.append((node.right, new_col))

        return list(result)
