# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sroot = self.serialized(root)
        ssubr = self.serialized(subRoot)
        combined = ssubr + "|" + sroot

        z_values = self.z_function(combined)
        len_sub = len(ssubr)

        for i in range(len_sub + 1, len(combined)):
            if z_values[i] == len_sub:
                return True
        return False

        return ssubr in sroot

    def serialized(self, node):
        if not node:
            return "$"
        return str(node.val) + self.serialized(node.left) + self.serialized(node.right)

    def z_function(self, s):
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)

        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return z