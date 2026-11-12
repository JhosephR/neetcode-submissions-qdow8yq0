class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        ans = []
        for n, f in freq.items():
            if f > len(nums) // 3:
                ans.append(n)
        return ans