class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        mx = max(nums)

        bucket = [0] * (mx - mn + 1)

        for n in nums:
            bucket[n - mn] += 1

        seen = 0
        for b in reversed(range(len(bucket))):
            if seen + bucket[b] >= k:
                return mn + b
            seen += bucket[b]
        return -1