class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            desired = target - n
            if desired in hashMap:
                return [hashMap[desired], i]
            hashMap[n] = i
        return []