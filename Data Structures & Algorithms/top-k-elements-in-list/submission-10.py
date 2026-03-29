class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        count = [[] for i in range(len(nums)+1)]
        res = []

        for n in nums:
            table[n] = 1 + table.get(n,0)

        for num, freq in table.items():
            count[freq].append(num)

        for lst in reversed(count):
            for n in lst:
                res.append(n)
                if len(res) == k:
                    return res