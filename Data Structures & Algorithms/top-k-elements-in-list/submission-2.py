class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap, freq = {}, [[] for i in range(len(nums) + 1)]

        for n in nums:                        # Find the frequency of numbers
            hashMap[n] = 1 + hashMap.get(n, 0)
        for n, c in hashMap.items():          # Flip the key->value pairs to value->key with number with the same count
            freq[c].append(n)
        ans = []
        for i in range(len(freq) - 1, 0, -1): # Iterate through the frequency list backwards
            for n in freq[i]:                 # Iterate through the sublist
                ans.append(n)                 
                if len(ans) == k:             # Stop when k numbers have been found
                    return ans