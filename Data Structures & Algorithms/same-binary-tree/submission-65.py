# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ser_p = self.serialize(p)
        ser_q = self.serialize(q)
        
        return ser_p == ser_q

    def serialize(self, root):
        if not root:
            return "$"
        return str(root.val) + self.serialize(root.left) + self.serialize(root.right)