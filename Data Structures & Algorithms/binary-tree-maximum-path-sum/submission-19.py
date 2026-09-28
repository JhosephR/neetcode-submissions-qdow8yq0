# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx, stack, path = root.val, [root], {None:0}
        while stack:
            node = stack[-1]
            if node.left and node.left not in path:
                stack.append(node.left)
            elif node.right and node.right not in path:
                stack.append(node.right)
            else:
                stack.pop()
                maxl = max(path[node.left], 0)
                maxr = max(path[node.right], 0)

                mx = max(mx, node.val + maxl + maxr)
                path[node] = node.val + max(maxl, maxr)
        return mx