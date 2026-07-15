# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack, height, diameter = [root], {None:0}, 0

        while stack:
            node = stack[-1]
            if node.left not in height:
                stack.append(node.left)
            elif node.right not in height:
                stack.append(node.right)
            else:
                node = stack.pop()
                left = height[node.left]
                right = height[node.right]

                diameter = max(diameter, left + right)
                height[node] = 1 + max(left, right)
        return diameter