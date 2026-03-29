class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for character in word:
                key[ord(character) - ord('a')] += 1
            
            key = tuple(key)
            if key in hashMap:
                hashMap[key].append(word)
            else:
                hashMap[key] = [word]
        return list(hashMap.values())