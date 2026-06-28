# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack, seen = [], {None:0}
        if root:
            stack.append(root)

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

                if abs(left - right) > 1:
                    return False
                seen[node] = 1 + max(left, right)
        return True