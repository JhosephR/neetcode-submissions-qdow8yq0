# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        while stack:
            r, s = stack.pop()
            if not r and not s:
                continue
            if not r or not s:
                return False
            if r.val != s.val:
                return False
            stack.append((r.left, s.left))
            stack.append((r.right, s.right))
        return True