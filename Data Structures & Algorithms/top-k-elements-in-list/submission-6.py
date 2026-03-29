class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap, bucket = defaultdict(int), {}

        for key in nums:
            hashMap[key] += 1

        for i in range(len(nums)+1):
            bucket[i] = []
        
        for key, value in hashMap.items():
            bucket[value].append(key)

        ans = []
        for freq, elem in reversed(bucket.items()):
            for num in elem:
                ans.append(num)
                if len(ans) == k:
                    return ans