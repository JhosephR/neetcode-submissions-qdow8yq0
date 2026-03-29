class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramHash = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for character in word:
                key[ord(character)-ord("a")] += 1
            anagramHash[str(key)].append(word)
            
        return list(anagramHash.values())