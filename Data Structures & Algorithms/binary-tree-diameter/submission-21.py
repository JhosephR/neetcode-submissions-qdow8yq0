# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack, seen, diameter = [root], {None:0}, 0

        while stack:
            node = stack[-1]
            if node.left not in seen:
                stack.append(node.left)
            elif node.right not in seen:
                stack.append(node.right)
            else:
                node = stack.pop()
                l_h = seen[node.left]
                r_h = seen[node.right]

                diameter = max(diameter, l_h + r_h)
                seen[node] = 1 + max(l_h, r_h)
        return diameter