class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for n, f in freq.items():
            bucket[f].append(n)
        
        ans = []
        for lst in reversed(bucket):
            for f in lst:
                ans.append(f)
                if len(ans) == k:
                    return ans
        return -1