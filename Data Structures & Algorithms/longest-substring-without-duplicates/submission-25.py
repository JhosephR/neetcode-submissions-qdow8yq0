class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        ans, l, setS = 0, 0, set()
        longest = 0
        for r in range(len(s)):
            while s[r] in setS:
                setS.remove(s[l])
                l += 1
            setS.add(s[r])
            longest = max(longest, r - l + 1)
        return longest