class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1, freq2, l = [0] * 26, [0] * 26, 0

        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1

        for r in range(len(s2)):
            freq2[ord(s2[r]) - ord('a')] += 1
            if (r - l + 1) == len(s1):
                if freq1 == freq2:
                    return True
                else:
                    freq2[ord(s2[l]) - ord('a')] -= 1
                    l += 1
        return False
