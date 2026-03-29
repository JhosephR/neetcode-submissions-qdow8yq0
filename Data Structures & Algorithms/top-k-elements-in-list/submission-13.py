class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans, freqMap = [], {}
        bucket = [[] for i in range(len(nums) + 1)]

        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)
        
        for n, f in freqMap.items():
            bucket[f].append(n)
        
        for lst in reversed(bucket):
            for n in lst:
                ans.append(n)
                if len(ans) == k:
                    return ans
        return