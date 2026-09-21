class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, matches, length, shortest, fS, fT = 0, 0, float("inf"), [0,0], {}, {}
        for c in t:
            fT[c] = 1 + fT.get(c, 0)

        for r in range(len(s)):
            fS[s[r]] = 1 + fS.get(s[r], 0)

            if s[r] in fT and fS[s[r]] == fT[s[r]]:
                matches += 1

            while matches == len(fT):
                if (r - l + 1) < length:
                    shortest = [l, r]
                    length = (r - l + 1)

                fS[s[l]] -= 1
                if s[l] in fT and fS[s[l]] < fT[s[l]]:
                    matches -= 1
                l += 1
        return s[shortest[0]:shortest[1] + 1] if length != float("inf") else ""