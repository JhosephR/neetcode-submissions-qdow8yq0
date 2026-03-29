class Solution:

    def encode(self, strs: List[str]) -> str:
        #"2#we3#say1#:3#yes"
        message = ""

        for s in strs:
            message += str(len(s)) + "#" + s
        return message

    def decode(self, s: str) -> List[str]:
        message = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            message.append(s[j + 1 : j + 1 + size])
            i = j + 1 + size
        return message