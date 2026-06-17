class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
            
        mapS, mapT, l, matches, ans, ansLen = {}, {}, 0, 0, [0,0], float("inf")

        for c in t:
            mapT[c] = 1 + mapT.get(c, 0)

        for r in range(len(s)):
            mapS[s[r]] = 1 + mapS.get(s[r], 0)

            if s[r] in mapT and mapS[s[r]] == mapT[s[r]]:
                matches += 1

            while matches == len(mapT):
                if (r - l + 1) < ansLen:
                    ans = [l, r]
                    ansLen = r - l + 1
                
                mapS[s[l]] -= 1
                if s[l] in mapT and mapS[s[l]] < mapT[s[l]]:
                    matches -= 1
                l += 1
        l, r = ans
        return s[l:r+1] if ansLen != float("inf") else ""