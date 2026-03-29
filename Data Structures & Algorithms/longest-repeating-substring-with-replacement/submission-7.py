class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, hashMap, maxF, longest = 0, {}, 0, 0

        for r in range(len(s)):
            hashMap[s[r]] = 1 + hashMap.get(s[r], 0)
            maxF = max(maxF, hashMap[s[r]])

            while (r - l + 1) - maxF > k:
                hashMap[s[l]] -= 1
                l += 1
            longest = max(longest, (r - l + 1))
        return longest
