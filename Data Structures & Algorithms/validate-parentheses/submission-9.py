class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        d = {'}':'{',')':'(',']':'['}

        for c in s:
            if c not in d:
                q.append(c)
                continue
            if not q or q[-1] != d[c]:
                return False
            q.pop()
        return not q