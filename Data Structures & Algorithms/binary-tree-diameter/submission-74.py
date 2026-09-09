# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(curr, depth):
            nonlocal diameter
            if not curr:
                return 0

            left = dfs(curr.left, 1 + depth)
            right = dfs(curr.right, 1 + depth)

            diameter = max(diameter, left + right)
            return 1 + max(left, right)
        dfs(root, 0)
        return diameter