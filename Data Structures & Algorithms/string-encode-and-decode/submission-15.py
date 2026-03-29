class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "" #5#study4#hard4#work4#hard
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        key = ""
        i = 0
        while i < len(s):
            if s[i] != "#":
                key += s[i]
                i += 1
            else:
                i += 1
                decoded.append(s[i:i+int(key)])
                i = i+int(key)
                key = ""
        return decoded

#["neet","code","love","you"]