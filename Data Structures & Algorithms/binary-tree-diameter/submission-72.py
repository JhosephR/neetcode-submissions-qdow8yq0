# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack, depth, diameter = [root], {None:0}, 0
        while stack:
            node = stack[-1]
            if node.left not in depth:
                stack.append(node.left)
            elif node.right not in depth:
                stack.append(node.right)
            else:
                node = stack.pop()
                left = depth[node.left]
                right = depth[node.right]

                diameter = max(diameter, left + right)
                depth[node] = 1 + max(left, right)
        return diameter