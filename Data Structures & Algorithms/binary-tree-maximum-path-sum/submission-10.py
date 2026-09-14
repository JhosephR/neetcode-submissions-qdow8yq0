# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        stack, depth, mx = [root], {None: 0}, root.val
        while stack:
            node = stack[-1]
            if node.left and node.left not in depth:
                stack.append(node.left)
            elif node.right and node.right not in depth:
                stack.append(node.right)
            else:
                stack.pop()
                ml = max(depth[node.left], 0)
                mr = max(depth[node.right], 0)
                depth[node] = node.val + max(ml, mr)

                mx = max(mx, node.val + ml + mr)
        return mx