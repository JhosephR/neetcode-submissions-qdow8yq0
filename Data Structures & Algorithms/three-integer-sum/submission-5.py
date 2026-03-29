class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, r, ans = 0, len(nums)-1, []
        nums.sort()

        while l < len(nums)-2:
            while l > 0 and l < len(nums) - 2 and nums[l] == nums[l-1]:
                l +=1
            m = l + 1
            r = len(nums)-1
            while m < r:
                sm = nums[l] + nums[m] + nums[r]
                if sm < 0:
                    m += 1
                elif sm > 0:
                    r -= 1
                else:
                    ans.append([nums[l],nums[m],nums[r]])
                    m += 1
                    while m < r and nums[m] == nums[m-1]:
                        m += 1
            l += 1
        return ans