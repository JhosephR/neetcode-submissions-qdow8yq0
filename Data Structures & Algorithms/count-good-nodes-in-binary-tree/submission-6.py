# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def height(curr, mx):
            if not curr:
                return None

            mx = max(curr.val, mx)

            height(curr.left, mx)
            height(curr.right, mx)

            if curr.val >= mx:
                self.ans += 1

        height(root, root.val)
        return self.ans