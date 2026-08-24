# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans, c = root, k
        def dfs(curr):
            nonlocal ans, c
            if not curr:
                return None
            
            dfs(curr.left)
            c -= 1
            if c == 0:
                ans = curr.val
                return
            dfs(curr.right)
        dfs(root)
        return ans