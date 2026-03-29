class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap, ans = {}, []
        bucket = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)

        for numb, freq in freqMap.items():
            bucket[freq].append(numb)

        for lst in reversed(bucket):
            for n in lst:
                ans.append(n)
                if len(ans) == k:
                    return ans