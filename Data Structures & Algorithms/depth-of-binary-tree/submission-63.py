# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(curr):
            if not curr:
                return 0
            
            left = height(curr.left)
            right = height(curr.right)

            return 1 + max(left, right)
        return height(root)