class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded = ''
        for string in strs:
            encoded += str(len(string)) + '#' + string
        return encoded

    def decode(self, s: str) -> list[str]:
        decoded = []
        i = 0
        j = 0
        while i < len(s):
            length = ''
            j = i
            while j < len(s):
                if s[j] != '#':
                    length+= s[j]
                    j += 1
                else:
                    i = j + 1
                    break
            start = i
            end = start + int(length)
            decoded.append(s[start:end])
            i = end
        return decoded