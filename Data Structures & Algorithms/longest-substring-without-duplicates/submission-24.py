class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest, setS = 0, 0, set()

        for r in range(len(s)):
            while s[r] in setS:
                setS.remove(s[l])
                l += 1
            setS.add(s[r])
            longest = max(longest, r - l + 1)
        return longest