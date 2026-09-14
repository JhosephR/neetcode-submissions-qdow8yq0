# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = root.val
        def dfs(node):
            nonlocal mx
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            ml = max(left, 0)
            mr = max(right, 0)

            mx = max(mx, node.val + ml + mr)
            return node.val + max(ml, mr)
        dfs(root)
        return mx