class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, longest, mp = 0, 1, {}
        for r in range(len(s)):
            mp[s[r]] = 1 + mp.get(s[r], 0)

            while r - l + 1 - max(mp.values()) > k:
                mp[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest