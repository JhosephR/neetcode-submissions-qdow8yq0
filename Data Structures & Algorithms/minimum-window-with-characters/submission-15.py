class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        fS, fT, l, matches, shortest = {}, {}, 0, 0, ""

        for c in t:
            fT[c] = 1 + fT.get(c, 0)

        for r in range(len(s)):
            fS[s[r]] = 1 + fS.get(s[r], 0)

            if s[r] in fT and fS[s[r]] == fT[s[r]]:
                matches += 1
            
            while matches == len(fT):
                if not shortest or (r - l + 1) < len(shortest):
                    shortest = s[l:r + 1]

                fS[s[l]] -= 1
                if s[l] in fT and fS[s[l]] < fT[s[l]]:
                    matches -= 1
                l += 1
        return shortest