class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        l, mapS, mapT, shortest, matches = 0, {}, {}, "", 0

        for c in t:
            mapT[c] = 1 + mapT.get(c, 0)

        for r, c in enumerate(s):
            mapS[c] = 1 + mapS.get(c, 0)

            if c in mapT and mapS[c] == mapT[c]:
                matches += 1

            while matches == len(mapT):
                if shortest == "":
                    shortest = s[l:r + 1]
                elif (r -l + 1) < len(shortest):
                    shortest = s[l:r + 1]
                mapS[s[l]] -= 1
                if s[l] in mapT and mapS[s[l]] < mapT[s[l]]:
                    matches -= 1
                l += 1
        return shortest