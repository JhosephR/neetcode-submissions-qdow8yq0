class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        mx = 0

        for n in nums:
            count = 0
            if n-1 not in nums:
                count += 1
                while n + count in nums:
                    count += 1
                mx = max(mx, count)
        return mx