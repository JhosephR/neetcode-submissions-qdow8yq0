class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = 1
        for i in range(1,len(nums)):
            ans[i] = nums[i-1] * prefix
            prefix *= nums[i-1]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i] * postfix
            postfix *= nums[i]
        return ans