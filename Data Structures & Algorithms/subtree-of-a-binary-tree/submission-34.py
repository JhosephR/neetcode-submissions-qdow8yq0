# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def serialized(self, node):
        if not node:
            return "$#"
        return "$" + str(node.val) + self.serialized(node.left) + self.serialized(node.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ser_root = self.serialized(root)
        ser_subRoot = self.serialized(subRoot)

        if ser_subRoot in ser_root:
            return True
        return False