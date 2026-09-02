class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = nums[0]
        while l <= r:
            m = l + (r - l) // 2
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])

            ans = min(ans, nums[m])        
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return ans