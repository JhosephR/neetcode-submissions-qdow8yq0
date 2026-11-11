class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        ans = sm = 0

        for n in nums:
            sm += n
            diff = sm - k

            if diff in prefixSum:
                ans += prefixSum[diff]
            prefixSum[sm] += 1
        return ans