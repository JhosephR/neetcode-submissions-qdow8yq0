class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, map1, map2 = 0, {}, {}

        for c in s1:
            map1[c] = 1 + map1.get(c, 0)

        for r in range(len(s2)):
            if s2[r] not in map1:
                map2 = {}
                continue
            
            if len(map2) == 0:
                l = r

            map2[s2[r]] = 1 + map2.get(s2[r], 0)
            if (r - l + 1) == len(s1):
                if map1 == map2:
                    return True
                else:
                    map2[s2[l]] -= 1
                    l += 1
        return False