class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest, numSet = 0, set(nums)

        for n in numSet:
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                longest = max(longest, length)
        return longest