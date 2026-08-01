# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def height(curr, depth):
            if not curr:
                return []
            
            if len(ans) == depth:
                ans.append([])

            ans[depth].append(curr.val)

            height(curr.left, depth + 1)
            height(curr.right, depth + 1)
        height(root, 0)
        return ans