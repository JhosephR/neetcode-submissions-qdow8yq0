class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet, l, longest = set(), 0, 0

        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            longest = max(longest, (r - l + 1))
        return longest