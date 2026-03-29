class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, longest, freqMap, maxF = 0, 0, {}, 0

        for r in range(len(s)):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)
            maxF = max(maxF, freqMap[s[r]])

            while (r - l + 1) - maxF > k:
                freqMap[s[l]] -= 1
                l += 1
            longest = max(longest, (r - l + 1))
        return longest