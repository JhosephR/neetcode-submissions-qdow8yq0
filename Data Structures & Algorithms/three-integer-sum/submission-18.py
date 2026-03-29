class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort the array
        ans = []

        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:  #skip elements already used for i
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                sm = v + nums[l] + nums [r]
                if sm < 0:
                    l += 1
                elif sm > 0:
                    r -= 1
                else:
                    ans.append([v, nums[l], nums[r]])
                    l += 1                      #increase and decrease both l and r pointers
                    r -= 1
                    while nums[l] == nums[l-1] and l < r: #skip elements already used for l
                        l += 1
        return ans