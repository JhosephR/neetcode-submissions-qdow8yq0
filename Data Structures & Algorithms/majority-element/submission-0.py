class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        maxF = [nums[0],1]  # [value, frequency]
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
            if maxF[1] < freq[n]:
                maxF = [n, freq[n]]
        return maxF[0]