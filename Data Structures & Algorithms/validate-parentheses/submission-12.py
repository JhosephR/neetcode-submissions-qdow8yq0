class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', '}':'{', ']':'['}
        q = []

        for i in range(len(s)):
            if s[i] not in d:
                q.append(s[i])
            elif s[i] in d:
                if not q:
                    return False
                elif q.pop() != d[s[i]]:
                    return False
        if q:
            return False
        else:
            return True