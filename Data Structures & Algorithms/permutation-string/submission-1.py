class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1, freq2, l, sm = {}, {}, 0, 0
        
        for c in s1:
            freq1[c] = 1 + freq1.get(c, 0)

        for r in range(len(s2)):
            if s2[r] not in freq1:
                freq2 = {}
                sm = 0
                continue
            if sm == 0:
                l = r

            freq2[s2[r]] = 1 + freq2.get(s2[r], 0)
            sm += 1
            if sm == len(s1):
                if freq1 == freq2:
                    return True
                else:
                    freq2[s2[l]] -= 1
                    sm -= 1
                    l += 1
        return False