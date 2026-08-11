# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(curr, mx):
            if not curr:
                return None
            
            if curr.val >= mx:
                mx = curr.val
                self.ans += 1
            
            dfs(curr.left, mx)
            dfs(curr.right, mx)
        dfs(root, root.val)
        return self.ans