class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            sm = target - nums[i]
            if sm in hashMap:
                return [hashMap[sm], i]
            else:
                hashMap[nums[i]] = i
        return []