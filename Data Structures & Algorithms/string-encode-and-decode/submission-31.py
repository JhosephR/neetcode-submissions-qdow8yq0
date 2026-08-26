class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        data = ""
        for s in strs:
            data += str(len(s)) + "#" + s
        return data

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        data = []
        i = j = 0
        while i < len(s):
            i = j
            while s[j] != "#" and j < len(s):
                j += 1
            size = int(s[i:j])
            i = j + 1
            j = i + size
            data.append(s[i:j])
            i = j + 1
        return data