class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord("a")] += 1
            key = tuple(key)

            hashMap[key].append(word)
        return list(hashMap.values())
            