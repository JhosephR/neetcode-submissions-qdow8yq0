class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1, f2, l = [0] * 26, [0] * 26, 0

        for c in s1:
            f1[ord(c) - ord('a')] += 1

        for r in range(len(s2)):
            f2[ord(s2[r]) - ord('a')] += 1

            if (r - l + 1) == len(s1):
                if f1 == f2:
                    return True
                else:
                    f2[ord(s2[l]) - ord('a')] -= 1
                    l += 1
        return False
