class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i in range(len(nums)):
            desired = target - nums[i]
            if desired in mp:
                return [mp[desired],i]
            else:
                mp[nums[i]] = i