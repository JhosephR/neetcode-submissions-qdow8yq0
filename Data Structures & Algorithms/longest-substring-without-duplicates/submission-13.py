class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest, indexMap = 0, 0, {}

        for r in range(len(s)):
            if s[r] in indexMap:
                l = max(indexMap[s[r]] + 1, l)
            indexMap[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest