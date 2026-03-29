class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""   #5#study4#hard4#work4#hard
        for string in strs:
            encoded += str(len(string)) + "#" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        
        i = 0
        while i < len(s):
            size = ""
            while s[i] != "#":
                size += s[i]
                i += 1
            i += 1
            decoded.append(s[i:i + int(size)])
            i = i + int(size)
        return decoded