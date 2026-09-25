class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, f1, f2, len1 = 0, [0] * 26, [0] * 26, len(s1)
        for c in s1:
            f1[ord(c) - ord('a')] += 1

        for r in range(len(s2)):
            f2[ord(s2[r]) - ord('a')] += 1

            if r - l + 1 == len1:
                if f1 == f2:
                    return True
                f2[ord(s2[l]) - ord('a')] -= 1
                l += 1
        return False