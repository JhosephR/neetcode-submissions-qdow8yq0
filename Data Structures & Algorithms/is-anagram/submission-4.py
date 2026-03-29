class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #s, t = list(s), list(t)
        d1, d2 = {}, {}

        for n in s:
            if n in d1:
                d1[n] += 1
            else:
                d1[n] = 1

        for m in t:
            if m in d2:
                d2[m] += 1
            else:
                d2[m] = 1

        if d1 == d2:
            return True
        return False