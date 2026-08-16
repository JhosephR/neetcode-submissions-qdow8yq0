# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = [(root, root.val)]
        ans = 0
        while q:
            node, mx = q.pop()

            if node.val >= mx:
                mx = node.val       # calculate mx only once
                ans += 1
            
            if node.left:
                q.append((node.left, mx))
            if node.right:
                q.append((node.right, mx))
        return ans