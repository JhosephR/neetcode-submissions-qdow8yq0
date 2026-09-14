# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        stack, path, mx = [root], {None: 0}, root.val
        while stack:
            node = stack[-1]
            if node.left and node.left not in path:
                stack.append(node.left)
            elif node.right and node.right not in path:
                stack.append(node.right)
            else:
                stack.pop()
                ml = max(path[node.left], 0)
                mr = max(path[node.right], 0)

                path[node] = node.val + max(ml, mr) # return best extendable path
                mx = max(mx, node.val + ml + mr)    # update best path through node
        return mx