class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, ans = 0, len(nums) - 1, nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                return min(ans, nums[l])

            m = l + ((r - l) // 2)
            ans = min(ans, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return ans