class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        i = 0
        ans = ""
        while i < n:
            ans += word1[i] + word2[i]
            i += 1

        if len(word1) < len(word2):
            ans += word2[i:]
            return ans

        ans += word1[i:]
        return ans