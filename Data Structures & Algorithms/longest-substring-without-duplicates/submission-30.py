class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, longest, charS = 0, 0, set()
        for r in range(len(s)):
            while s[r] in charS:
                charS.remove(s[l])
                l += 1
            charS.add(s[r])
            longest = max(longest, r - l + 1)
        return longest