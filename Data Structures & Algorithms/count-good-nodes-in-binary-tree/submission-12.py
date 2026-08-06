# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        ans = 0
        while stack:
            node, mx = stack.pop()
            if node.val >= mx:
                mx = node.val
                ans += 1
            
            if node.left:
                stack.append((node.left, mx))
            if node.right:
                stack.append((node.right, mx))
        return ans