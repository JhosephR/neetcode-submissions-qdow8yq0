class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 1
        while True:
            if ans not in nums:
                return ans
            ans += 1
        return -1