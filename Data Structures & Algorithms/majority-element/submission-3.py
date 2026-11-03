class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = count = 0

        for n in nums:
            if count == 0:
                ans = n
            count += (1 if n == ans else -1)
        return ans
