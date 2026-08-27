class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums, ans = sorted(nums), []
        for i, v in enumerate(nums):
            if i > 0 and nums[i-1] == v:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sm = v + nums[l] + nums[r]
                if sm < 0:
                    l += 1
                elif sm > 0:
                    r -= 1
                else:
                    ans.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return ans
