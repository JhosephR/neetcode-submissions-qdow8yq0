class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freqMap, longest = {}, 0

        for n in nums:
            freqMap[n] = 1 + freqMap.get(n,0)

        for n in nums:
            if n-1 not in freqMap:
                length = 1
                while n+length in freqMap:
                    length += 1
                longest = max(longest,length)
        return longest