class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, matches, length, short, mpS, mpT = 0, 0, float("inf"), [-1,-1], {}, {}
        for c in t:
            mpT[c] = 1 + mpT.get(c, 0)

        lenT = len(mpT)
        for r in range(len(s)):
            mpS[s[r]] = 1 + mpS.get(s[r], 0)

            if s[r] in mpT and mpS[s[r]] == mpT[s[r]]:
                matches += 1

            while matches == lenT:
                if r - l + 1 < length:
                    short = [l, r]
                    length = r - l + 1
                
                mpS[s[l]] -= 1
                if s[l] in mpT and mpS[s[l]] < mpT[s[l]]:
                    matches -= 1
                l += 1
        return s[short[0]:short[1] + 1] if length != float("inf") else ""