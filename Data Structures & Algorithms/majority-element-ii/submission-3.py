class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1    # Count frequencies

            if len(freq) > 2:
                new_freq = defaultdict(int) # temp map
                for n in freq:
                    freq[n] -= 1    # decrease all by 1

                    if freq[n] > 0 :    # Keep non-zero counts
                        new_freq[n] = freq[n]
                freq = new_freq
        
        ans = []
        for n in freq:  # Recount original occurences
            if nums.count(n) > len(nums) // 3:  # Compare with n // 3 
                ans.append(n)
        return ans

