class Solution:

    def encode(self, strs: List[str]) -> str:
        message = "" #5#study4#hard4#work4#hard
        for word in strs:
            message += str(len(word)) + "#" + word
        return message

    def decode(self, s: str) -> List[str]:
        message = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            i = j + 1
            message.append(s[i: i + size])
            i = i + size
        return message