class Solution:

    def encode(self, strs: List[str]) -> str:
        message = "" #5#study4#hard4#work4#hard
        for s in strs:
            message += str(len(s)) + '#' + s
        print(message)
        return message

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            size = str(s[i:j])
            i = j + 1
            j = i + int(size)
            decoded.append(s[i:j])
            i = j
        return decoded