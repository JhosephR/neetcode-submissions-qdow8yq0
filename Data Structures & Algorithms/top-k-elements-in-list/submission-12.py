class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_sort = [[] for i in range(len(nums) + 1)]
        freqTable, ans = {}, []

        for n in nums:
            freqTable[n] = 1 + freqTable.get(n,0)
        
        for num, freq in freqTable.items():
            bucket_sort[freq].append(num)

        for lst in reversed(bucket_sort):
            for num in lst:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return