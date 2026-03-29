class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        l, r, longest = 0, 0, 0

        while r < len(s):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1

            hashSet.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        print(hashSet)
        return longest