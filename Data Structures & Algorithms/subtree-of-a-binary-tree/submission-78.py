# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, r, s):
        q = deque([(r, s)])
        while q:
            r, s = q.popleft()
            if not r and not s:
                continue
            if not r or not s:
                return False
            if r.val != s.val:
                return False
            q.append((r.left, s.left))
            q.append((r.right, s.right))
        return True