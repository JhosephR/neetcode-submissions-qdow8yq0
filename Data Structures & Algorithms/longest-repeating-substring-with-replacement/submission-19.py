class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxF, longest, mp = 0, 0, 0, {}
        for r in range(len(s)):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            maxF = max(maxF, mp[s[r]])

            while r - l + 1 - maxF > k:
                mp[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest