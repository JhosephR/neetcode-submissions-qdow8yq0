class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', '}':'{', ']':'['}
        q = []

        for c in s:
            if c not in d:
                q.append(c)
            elif c in d:
                if not q or q.pop() != d[c]:
                    return False
        return not q