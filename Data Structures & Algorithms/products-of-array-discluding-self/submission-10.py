class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]  # [1,1,2,8]
        pos = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= pos
            pos *= nums[i]  # [48,24,12,8]
        return ans