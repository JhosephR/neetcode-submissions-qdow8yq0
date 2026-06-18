class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freS, freT, matches, ans, ansLen, l = {}, {}, 0, [0,0], float("inf"), 0
        for c in t:
            freT[c] = 1 + freT.get(c, 0)

        for r in range(len(s)):
            freS[s[r]] = 1 + freS.get(s[r], 0)
            
            if s[r] in freT and freS[s[r]] == freT[s[r]]:
                matches += 1

            while matches == len(freT):
                if (r - l + 1) < ansLen:
                    ans = [l, r]
                    ansLen = r - l + 1
                
                freS[s[l]] -= 1
                if s[l] in freT and freS[s[l]] < freT[s[l]]:
                    matches -= 1
                l += 1
        l, r = ans
        return s[l:r+1] if ansLen < float("inf") else ""