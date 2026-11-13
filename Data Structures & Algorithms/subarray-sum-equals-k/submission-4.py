class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        ans = sm = 0

        for n in nums:
            sm += n
            diff = sm - k
            
            ans += (prefixSum.get(diff, 0))
            prefixSum[sm] = 1 + prefixSum.get(sm, 0)
        return ans