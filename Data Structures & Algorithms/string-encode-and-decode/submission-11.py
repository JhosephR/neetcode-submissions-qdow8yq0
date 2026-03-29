class Solution:

    def encode(self, strs: List[str]) -> str:
        #"2#we3#say1#:3#yes"
        message = ""

        for s in strs:
            message += str(len(s)) + "#" + s
        return message

    def decode(self, s: str) -> List[str]:
        message = []
        key = ""
        c = 0

        while c < len(s):
            if s[c].isdigit():
                key += s[c]
                c += 1
            else:
                c += 1
                message.append(s[int(c):int(c)+int(key)])
                c += int(key)
                key = ""
        return message