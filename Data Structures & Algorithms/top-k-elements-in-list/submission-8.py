class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        bucket = [[] for i in range(len(nums)+1)]

        for number in nums:
            freqMap[number] = 1 + freqMap.get(number,0)

        for number, count in freqMap.items():
            bucket[count].append(number)

        res = []
        for array in range(len(bucket)-1,0,-1):
            for number in bucket[array]:
                res.append(number)
                if len(res) == k:
                    return res