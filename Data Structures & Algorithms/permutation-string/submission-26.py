class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        fre1, fre2, l = [0] * 26, [0] * 26, 0
        for c in s1:
            fre1[ord(c) - ord('a')] += 1

        for r in range(len(s2)):
            fre2[ord(s2[r]) - ord('a')] += 1

            if (r - l + 1) == len(s1):
                if fre1 == fre2:
                    return True
                else:
                    fre2[ord(s2[l]) - ord('a')] -= 1
                    l += 1
        return False