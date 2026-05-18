class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap, ans = {}, []

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)
        
        bucket = [[] for i in range(len(nums)+1)]
        for n, f in hashMap.items():
            bucket[f].append(n)

        for lst in reversed(bucket):
            for n in lst:
                ans.append(n)
                if len(ans) == k:
                    return ans