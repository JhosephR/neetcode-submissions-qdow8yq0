# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count, ans = 0, root.val
        def dfs(curr):
            nonlocal count, ans

            if not curr:
                return None
            
            dfs(curr.left)
            count += 1
            if count == k:
                ans = curr.val
                return
            dfs(curr.right)
        dfs(root)
        return ans