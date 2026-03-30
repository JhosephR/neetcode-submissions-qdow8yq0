class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest, hashMap = 0, 0, {}

        for r in range(len(s)):
            if s[r] in hashMap:
                l = max(l, hashMap[s[r]] + 1)
            hashMap[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest