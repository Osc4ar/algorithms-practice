# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1. Take element 0 in preorder and that is the root
2. Find the element on the inorder array and the left side are the left nodes and the same for the right
3. On the preorder array separate the left and right nodes based on the numbers found in the inorder
4. Repeat step 1 for right and left
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(val=preorder[0])

        root = TreeNode(val=preorder[0])

        root_index = 0
        for index, value in enumerate(inorder):
            if root.val == value:
                root_index = index
                break

        left_preorder = preorder[1:root_index+1]
        right_preorder = preorder[root_index+1:]

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
