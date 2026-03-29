class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength, hashSet = 0, set(nums)

        for n in hashSet:
            if n - 1 not in hashSet:
                length = 1
                while n + length in hashSet:
                    length += 1
                maxLength = max(maxLength, length)
        return maxLength