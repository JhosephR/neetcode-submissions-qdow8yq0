# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ser_r = self.serialize(root)
        ser_s = self.serialize(subRoot)

        return ser_s in ser_r

    def serialize(self, root):
        if not root:
            return "$"
        return str(root.val) + self.serialize(root.left) + self.serialize(root.right)