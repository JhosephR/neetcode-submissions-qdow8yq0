class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        sorted_d = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
        ans = list(sorted_d.keys())[:k]
        return ans