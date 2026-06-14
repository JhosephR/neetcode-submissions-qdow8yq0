class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, length, seen = 0, 0, 0, set()
        while r < len(s):
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
            length = max(length, r - l)
            seen.remove(s[l])
            l += 1
        return length