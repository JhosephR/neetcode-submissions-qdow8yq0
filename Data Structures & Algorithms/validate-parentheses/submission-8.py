class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        d = {'}':'{',')':'(',']':'['}

        for c in s:
            if c in d:
                if q and q[-1] == d[c]:
                    q.pop()
                    continue
                else:
                    return False
            else:
                q.append(c)
        return True if not q else False