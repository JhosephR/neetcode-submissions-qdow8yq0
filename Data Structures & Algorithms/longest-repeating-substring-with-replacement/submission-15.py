class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapS, longest, l, maxF = {}, 0, 0, 0

        for r in range(len(s)):
            mapS[s[r]] = 1 + mapS.get(s[r], 0)
            maxF = max(maxF, mapS[s[r]])

            while (r - l + 1) - maxF > k:
                mapS[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        return longest