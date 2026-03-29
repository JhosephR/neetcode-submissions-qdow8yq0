class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            desired = target - nums[i]
            if desired in hashMap:
                return [hashMap[desired], i]
            else:
                hashMap[nums[i]] = i
        return []