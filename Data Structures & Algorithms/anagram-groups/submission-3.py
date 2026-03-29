class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramHash = {}

        for word in strs:
            hashMap = {}
            for letter in word:
                if letter in hashMap:
                    hashMap[letter] += 1
                else:
                    hashMap[letter] = 1

            freqArray = [0] * 26
            for key, value in hashMap.items():
                freqArray[ord(key)-97] = value
            
            freqArray = tuple(freqArray)
            if freqArray in anagramHash:
                anagramHash[freqArray].append(word)
            else:
                anagramHash[freqArray] = [word]
        return list(anagramHash.values())