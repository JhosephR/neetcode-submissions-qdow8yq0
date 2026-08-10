# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ser_r = self.serialize(root)
        ser_s = self.serialize(subRoot)
        combined = ser_s + "|" + ser_r

        return self.z_function(combined, len(ser_s))

    def z_function(self, s, len_s):
        n = len(s)
        z = [0] * n
        l, r = 0, 0

        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[l - i])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
            if i >= len_s + 1 and z[i] == len_s:
                return True
        return False

    def serialize(self, root):
        if not root:
            return "$"
        return str(root.val) + self.serialize(root.left) + self.serialize(root.right)