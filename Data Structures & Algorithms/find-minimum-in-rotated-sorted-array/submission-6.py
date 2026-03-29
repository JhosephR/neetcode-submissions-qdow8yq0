class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = nums[0]
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[l] < nums[r]:
                return min(ans,nums[l])
            if nums[l] <= nums[m]:
                ans = min(ans, nums[l])
                l = m + 1
            elif nums[m] < nums[r]:
                ans = min(ans, nums[m])
                r = m - 1
        return ans