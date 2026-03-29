class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = nums[0]

        while l <= r:
            if nums[l] < nums[r]:   # sorted
                return min(ans, nums[l])

            m = l + ((r - l) // 2)
            ans = min(ans, nums[m])
            if nums[l] <= nums[m]:  # left half?
                l = m + 1           # go to the right
            else:                   # right half?
                r = m - 1           # go to the left
        return ans