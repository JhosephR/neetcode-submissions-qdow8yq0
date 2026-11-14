class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        mx = max(nums)
        ans = 1

        for i in range(1, mx + 1):
            if ans not in nums:
                return ans
            ans += 1
        return ans