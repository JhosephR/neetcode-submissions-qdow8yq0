class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, matches, shortest, ft, fs = 0, 0, "", {}, {}
        for c in t:
            ft[c] = 1 + ft.get(c, 0)
        
        for r in range(len(s)):
            fs[s[r]] = 1 + fs.get(s[r], 0)

            if s[r] in ft and fs[s[r]] == ft[s[r]]:
                matches += 1

            while matches == len(ft):
                if shortest == "":
                    shortest = s[l:r + 1]
                elif r - l + 1 < len(shortest):
                    shortest = s[l:r + 1]
                    
                fs[s[l]] -= 1
                if s[l] in ft and fs[s[l]] < ft[s[l]]:
                    matches -= 1
                l += 1
        return shortest