# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack, seen = [], {}
        if root:
            stack.append(root)

        while stack:
            node = stack[-1]
            if node.left and node.left not in seen:
                stack.append(node.left)
            elif node.right and node.right not in seen:
                stack.append(node.right)
            else:
                node = stack.pop()
                left = seen.get(node.left,0)
                right = seen.get(node.right,0)

                if abs(left - right) > 1:
                    return False
                seen[node] = 1 + max(left, right)
        return True