class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, ans = [1], [1], []

        for i in range(len(nums)-1):
            left.append(left[i] * nums[i])
            right.append(right[i] * nums[-i-1])
        
        for i in range(len(nums)):
            ans.append(left[i] * right[-i-1])
        return ans