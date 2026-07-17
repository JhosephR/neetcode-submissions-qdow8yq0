# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ser_p = self.serialized(p)
        ser_q = self.serialized(q)
        return ser_q == ser_p

    def serialized(self, root):
        if not root:
            return "$"
        return "$" + str(root.val) + self.serialized(root.left) + self.serialized(root.right)