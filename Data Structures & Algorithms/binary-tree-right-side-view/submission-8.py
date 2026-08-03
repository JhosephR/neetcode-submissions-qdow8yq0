# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []

        def height(curr, depth):
            if not curr:
                return None

            if len(ans) == depth:
                ans.append(curr.val)

            height(curr.right, depth + 1)
            height(curr.left, depth + 1)
        height(root, 0)
        return ans