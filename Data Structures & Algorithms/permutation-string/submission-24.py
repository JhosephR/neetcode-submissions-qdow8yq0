class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1, f2, l = {}, {}, 0

        for c in s1:
            f1[c] = 1 + f1.get(c, 0)

        for r in range(len(s2)):
            f2[s2[r]] = 1 + f2.get(s2[r], 0)

            if (r - l + 1) == len(s1):
                if f1 == f2:
                    return True
                else:
                    f2[s2[l]] -= 1
                    if f2[s2[l]] == 0:
                        del f2[s2[l]]
                    l += 1
        return False