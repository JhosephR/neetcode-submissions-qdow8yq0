class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

            if len(freq) > 2:
                new_freq = defaultdict(int)
                for n in freq:
                    freq[n] -= 1

                    if freq[n] > 0 :
                        new_freq[n] = freq[n]
                freq = new_freq
        
        ans = []
        for n in freq:
            if nums.count(n) > len(nums) // 3:
                ans.append(n)
        return ans

