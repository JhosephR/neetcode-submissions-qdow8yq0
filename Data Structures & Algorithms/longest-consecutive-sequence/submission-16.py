class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest, length, hashSet = 0, 0, set(nums)

        for n in nums:
            if n - 1 not in hashSet:
                length = 1
                while n + length in hashSet:
                    length += 1
                longest = max(longest,length)
            hashSet.add(n)
        return longest