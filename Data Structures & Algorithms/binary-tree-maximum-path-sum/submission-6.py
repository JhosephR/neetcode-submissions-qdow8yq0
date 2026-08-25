# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        stack, seen, mx = [root], {None: 0}, float("-inf")
        while stack:
            node = stack[-1]            
            if node.left and node.left not in seen:
                stack.append(node.left)
            elif node.right and node.right not in seen:
                stack.append(node.right)
            else:
                stack.pop()
                lmax = max(seen[node.left], 0)
                rmax = max(seen[node.right], 0)
                
                mx = max(mx, node.val + lmax + rmax)
                seen[node] = node.val + max(lmax, rmax) 
        return mx   