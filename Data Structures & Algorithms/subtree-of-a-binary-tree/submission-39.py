# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ser_root = self.serialized(root)
        ser_subr = self.serialized(subRoot)
        print(ser_root, ser_subr)
        return ser_subr in ser_root

    def serialized(self, root):
        if not root:
            return "$"
        return str(root.val) + self.serialized(root.left) + self.serialized(root.right)