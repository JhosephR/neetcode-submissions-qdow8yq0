class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        l, map1, map2 = 0, {}, {}
        for c in s1:
            map1[c] = 1 + map1.get(c, 0)

        for r in range(len(s2)):
            map2[s2[r]] = 1 + map2.get(s2[r], 0)

            if r - l + 1 == len(s1):
                if map1 == map2:
                    return True
                else:
                    map2[s2[l]] -= 1
                    if map2[s2[l]] == 0:
                        del map2[s2[l]]
                    l += 1
        return False