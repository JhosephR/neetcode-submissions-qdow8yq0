class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index, number in enumerate(nums):
            difference = target - number
            if difference in hashMap:
                return [hashMap[difference], index]
            hashMap[number] = index