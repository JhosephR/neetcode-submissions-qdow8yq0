class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sort first O(nlogn)
        ans = []

        for index, value in enumerate(nums):     #O(n^2)
            if index > 0 and value == nums[index-1]:
                continue

            left, right = index+1, len(nums)-1
            while left < right:                 #two pointer technique
                suma = value + nums[left] + nums[right]
                if suma < 0:
                    left += 1
                elif suma > 0:
                    right -= 1
                else:
                    ans.append([value, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                         left += 1
        return ans