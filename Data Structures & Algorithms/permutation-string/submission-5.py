class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1, freq2, l = {}, {}, 0
        
        for c in s1:
            freq1[c] = 1 + freq1.get(c, 0)

        for r in range(len(s2)):    # find a valid character
            if s2[r] not in freq1:  # reset dictionary if unwanted character found
                freq2 = {}
                continue

            if len(freq2) == 0:     # jump to beginning of valid substring 
                l = r

            freq2[s2[r]] = 1 + freq2.get(s2[r], 0) # start counting characters

            if (r - l + 1) == len(s1):  # is window size the right lenght?
                if freq1 == freq2:  # compare matches
                    return True
                else:
                    freq2[s2[l]] -= 1 # remove/decrease left character
                    l += 1            # move left pointer to next character
        return False