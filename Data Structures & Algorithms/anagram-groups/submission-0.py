class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            binaryForm = [0] * 26 # represent a binary representation of a string from a-z
            for c in s:
                binaryForm[ord(c) - ord('a')] += 1
            ans[tuple(binaryForm)].append(s)
        return ans.values()