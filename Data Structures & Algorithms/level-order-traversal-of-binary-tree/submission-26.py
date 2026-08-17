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
        def dfs(curr, depth):
            if not curr:
                return None
            if len(ans) == depth:
                ans.append([])
            ans[depth].append(curr.val)

            dfs(curr.left, depth + 1)
            dfs(curr.right, depth + 1)
        dfs(root, 0)
        return ans