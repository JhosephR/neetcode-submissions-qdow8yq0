class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency, bucket = defaultdict(int), {}

        for key in nums:
            frequency[key] += 1

        for j in range(len(nums)+1): # Create a bucket of n+1 lenght
            bucket[j] = []
        
        for num, freq in frequency.items(): # group the numbers based on their frequency from 1 to n
            bucket[freq].append(num)

        ans = []
        for frequ, nlist in reversed(bucket.items()):
            for element in nlist:
                ans.append(element)
                if len(ans) == k:
                    return ans