# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = root.val
        def path(node):
            nonlocal mx
            if not node:
                return 0

            mxl = max(path(node.left), 0)
            mxr = max(path(node.right), 0)

            mx = max(mx, node.val + mxl + mxr)
            return node.val + max(mxl, mxr)
        path(root)
        return mx