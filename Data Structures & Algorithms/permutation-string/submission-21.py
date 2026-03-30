class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        l, arr1, arr2 = 0, [0] * 26, [0] * 26

        for i in range(len(s1)):
            arr1[ord(s1[i]) - ord('a')] += 1

        for r in range(len(s2)):
            arr2[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 == len(s1):
                if arr1 == arr2:
                    return True
                else:
                    arr2[ord(s2[l]) - ord('a')] -= 1
                    l += 1
        return False