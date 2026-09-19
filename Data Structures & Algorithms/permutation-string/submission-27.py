class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1, mp2 = {}, {}
        for c in s1:
            mp1[c] = 1 + mp1.get(c, 0)
        
        l = 0
        for r in range(len(s2)):
            mp2[s2[r]] = 1 + mp2.get(s2[r], 0)
            
            if (r - l + 1) == len(s1):
                if mp1 == mp2:
                    return True

                mp2[s2[l]] -= 1
                if mp2[s2[l]] == 0:
                    del mp2[s2[l]]
                l += 1
        return False