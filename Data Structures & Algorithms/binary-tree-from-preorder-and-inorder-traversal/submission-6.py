# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashMap = {v: i for i, v in enumerate(inorder)}
        p = 0
        def dfs(l, r):
            nonlocal p
            if l > r:
                return None
            
            root = TreeNode(preorder[p])
            p += 1
            mid = hashMap[root.val]
            
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(inorder) - 1)