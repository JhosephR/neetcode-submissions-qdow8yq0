class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, freqTable, maxF, longest = 0, {}, 0, 0

        for r in range(len(s)):
            freqTable[s[r]] = 1 + freqTable.get(s[r], 0)
            maxF = max(maxF, freqTable[s[r]])

            while (r - l + 1) - maxF > k:
                freqTable[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest