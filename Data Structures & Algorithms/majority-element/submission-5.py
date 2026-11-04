class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = count = 0
        for n in nums:
            if count == 0:
                num = n
            count += (1 if num == n else -1)
        return num