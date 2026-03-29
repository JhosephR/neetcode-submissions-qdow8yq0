class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, mapS, mapT, count, shortest = 0, {}, {}, 0, ""

        for c in t:
            mapT[c] = 1 + mapT.get(c, 0)

        for r in range(len(s)):
            mapS[s[r]] = 1 + mapS.get(s[r], 0)

            if s[r] in mapT and mapS[s[r]] == mapT[s[r]]:
                count += 1

            while count == len(mapT):
                if shortest == "":
                    shortest = s[l:r + 1]
                elif (r - l + 1) < len(shortest):
                    shortest = s[l:r + 1]
                mapS[s[l]] -= 1
                if s[l] in mapT and mapS[s[l]] < mapT[s[l]]:
                    count -= 1
                l += 1
        return shortest