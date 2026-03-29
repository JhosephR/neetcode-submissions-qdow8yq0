class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        pos = 1

        for i in range(len(nums)-1):
            ans.append(ans[i] * nums[i])

        for j in range(len(ans)-1,-1,-1):
            ans[j] *= pos
            pos *= nums[j]

        return ans