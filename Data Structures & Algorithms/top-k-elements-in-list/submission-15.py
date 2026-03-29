class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq, ans = {}, []
        bucket = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        for n, f in freq.items():
            bucket[f].append(n)

        for lst in reversed(bucket):
            for n in lst:
                ans.append(n)
                if len(ans) == k:
                    return ans
        return []