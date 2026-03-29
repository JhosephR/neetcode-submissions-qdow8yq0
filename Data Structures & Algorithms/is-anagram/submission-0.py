class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = dict(), dict()
        
        for l in s:
            if l in d1:
                d1[l] += 1
            else:
                d1[l] = 1
        
        for k in t:
            if k in d2:
                d2[k] += 1
            else:
                d2[k] = 1

        if d1 == d2:
            return True
        return False