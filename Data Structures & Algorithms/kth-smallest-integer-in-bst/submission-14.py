# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c = k
        ans = root
        def dfs(curr):
            nonlocal c, ans
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