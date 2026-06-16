class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest, seen = 0, 0, set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, r - l + 1)
        return longest