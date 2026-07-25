# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ser_r = self.serialized(root)
        ser_s = self.serialized(subRoot)
        combined = ser_s + "|" + ser_r

        return self.z_function(combined, len(ser_s))

    def z_function(self, s, len_s):
        n = len(s)
        l, r, = 0, 0
        z = [0] * n

        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
            if i >= len_s + 1 and z[i] == len_s:
                return True
        return False

    def serialized(self, root):
        if not root:
            return "$"
        return str(root.val) + self.serialized(root.left) + self.serialized(root.right)