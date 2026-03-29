class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue

            j, k = i+1, len(nums)-1
            while j < k:
                sm = v + nums[j] + nums[k]
                if sm < 0:
                    j += 1
                elif sm > 0:
                    k -= 1
                else:
                    ans.append([v, nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return ans