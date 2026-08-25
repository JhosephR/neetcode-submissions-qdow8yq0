# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root] 
        seen = {None: 0}   # <- height only, instead of {None: (0, 0)}
        diameter = 0

        while stack:
            node = stack[-1]
            if node.left and node.left not in seen:
                stack.append(node.left)
            elif node.right and node.right not in seen:
                stack.append(node.right)
            else:
                stack.pop()
                left = seen[node.left]        # left height
                right = seen[node.right]      # right height

                diameter = max(diameter, left + right)
                seen[node] = 1 + max(left, right)
        return diameter