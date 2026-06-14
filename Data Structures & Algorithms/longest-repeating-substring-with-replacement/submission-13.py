class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, length, freqMap, maxF = 0, 0, {}, 0

        for r in range(len(s)):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)
            maxF = max(maxF, freqMap[s[r]])

            while (r - l + 1) - maxF > k:
                freqMap[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)
        return length