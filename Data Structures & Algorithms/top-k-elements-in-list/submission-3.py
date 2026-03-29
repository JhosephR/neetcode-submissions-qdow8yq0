class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n, 0)
            
        sorted_d = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
        ans = list(sorted_d.keys())[:k]
        return ans