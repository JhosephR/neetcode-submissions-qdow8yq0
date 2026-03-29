class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1, d2 = {}, {}
        for c in range(len(s)):
            d1[s[c]] = 1 + d1.get(s[c], 0)
            d2[t[c]] = 1 + d2.get(t[c], 0)
        return d1 == d2