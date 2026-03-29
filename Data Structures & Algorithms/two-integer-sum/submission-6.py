class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in myMap:
                return [myMap[diff], index]
            myMap[number] = index