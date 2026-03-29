class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap, tMap = {}, {}
        for character in s:
            if character in sMap:
                sMap[character] += 1
            else:
                sMap[character] = 1

        for character in t:
            if character in tMap:
                tMap[character] += 1
            else:
                tMap[character] = 1
        
        for c in sMap:
            if c not in tMap:
                return False
            if sMap[c] != tMap[c]:
                return False
        return True