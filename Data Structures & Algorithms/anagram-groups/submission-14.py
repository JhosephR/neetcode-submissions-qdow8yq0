class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] += 1
            map[tuple(key)].append(word)
        return list(map.values())