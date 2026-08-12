# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        self.n = 0
        def dfs(curr):
            if not curr:
                return None
            
            dfs(curr.left)
            ans.append(curr.val)
            self.n += 1
            if self.n == k:
                return curr.val
            dfs(curr.right)
        dfs(root)
        return ans[k - 1]