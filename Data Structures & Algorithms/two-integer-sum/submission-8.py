class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, v in enumerate(nums):
            desired = target - v
            if desired in seen:
                return [seen[desired], i]
            seen[v] = i
        return []