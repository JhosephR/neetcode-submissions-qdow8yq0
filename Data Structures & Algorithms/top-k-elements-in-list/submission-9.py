class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        count = [[] for i in range(len(nums)+1)]
        arrk = []

        for n in nums:
            table[n] = 1 + table.get(n,0)

        for num, freq in table.items():
            count[freq].append(num)

        for lst in reversed(count):
            for n in lst:
                if n not in arrk:
                    arrk.append(n)
                    if len(arrk) == k:
                        return arrk