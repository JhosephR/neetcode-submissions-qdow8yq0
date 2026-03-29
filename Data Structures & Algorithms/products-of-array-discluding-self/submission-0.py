class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        indexes, ans, totalMul = [], [], 1
        for i in range(len(nums)):
            if nums[i] == 0:
                indexes.append(i)
            if len(indexes) == 2:
                ans = [0 for _ in range(len(nums))]
                return ans
        if len(indexes) == 1:
            for i in range(len(nums)):
                if i != indexes[0]:
                    totalMul *= nums[i]
            ans = [0 for _ in range(len(nums))]
            ans[indexes[0]] = totalMul
            return ans
        else:
            for i in range(len(nums)):
                totalMul *= nums[i]
            for n in nums:
                ans.append(totalMul//n)
            return ans