class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freqMap = [0] * 26
        for i in range(len(s)):
            freqMap[ord(s[i]) - ord('a')] += 1
            freqMap[ord(t[i]) - ord('a')] -= 1

        for val in freqMap:
            if val != 0:
                return False
        return True