class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest = 0, 0
        hashSet = set()

        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            longest = max(longest, r - l + 1)
        return longest