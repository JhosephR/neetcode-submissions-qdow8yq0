# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def depth(curr):
            if not curr:
                return 0
            left = depth(curr.left)
            if left == -1:
                return -1

            right = depth(curr.right)
            if right == -1 or abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
        return depth(root) > -1