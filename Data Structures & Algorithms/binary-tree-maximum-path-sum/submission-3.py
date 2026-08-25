# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        stack, seen, mx = [root], {None:0}, root.val
        while stack:
            node = stack[-1]
            if node.left not in seen:
                stack.append(node.left)
            elif node.right not in seen:
                stack.append(node.right)
            else:
                node = stack.pop()
                left = seen[node.left]
                right = seen[node.right]
                leftMax = max(left, 0)
                rightMax = max(right, 0)

                mx = max(mx, node.val + leftMax + rightMax)
                seen[node] = node.val + max(leftMax, rightMax)
        return mx