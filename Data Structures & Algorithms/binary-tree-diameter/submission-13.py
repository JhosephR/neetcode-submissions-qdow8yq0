# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack, seen, diam = [root], {None:0}, 0

        while stack:
            node = stack[-1]
            if node.left not in seen:
                stack.append(node.left)
            elif node.right not in seen:
                stack.append(node.right)
            else:
                node = stack.pop()
                l_height = seen[node.left]
                r_height = seen[node.right]

                diam = max(diam, l_height + r_height)
                seen[node] = 1 + max(l_height, r_height)
        return diam