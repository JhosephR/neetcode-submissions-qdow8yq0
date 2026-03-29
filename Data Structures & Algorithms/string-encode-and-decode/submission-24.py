class Solution:

    def encode(self, strs: List[str]) -> str:
        message = "" # 5#study4#hard4#work4#hard
        for word in strs:
            message += str(len(word)) + "#" + word
        return message

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            size = ""
            while s[i] != "#":
                size += s[i]
                i += 1
            size = int(size)
            i += 1
            decoded.append(s[i: i + size])
            i = i + size
        return decoded