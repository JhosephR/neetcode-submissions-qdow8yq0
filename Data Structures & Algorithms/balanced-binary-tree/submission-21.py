# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack, height = [], {None:0}
        if root:
            stack.append(root)

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

                if abs(left - right) > 1:
                    return False

                height[node] = 1 + max(left, right)
        return True