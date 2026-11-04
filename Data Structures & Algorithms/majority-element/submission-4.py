class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        mx = [nums[0], 1]

        for i, n in enumerate(nums):
            freq[n] = 1 + freq.get(n, 0)
            if freq[n] > mx[1]:
                mx = [n, freq[n]]
        return mx[0]