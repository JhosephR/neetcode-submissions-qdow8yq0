class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        q = []
        d = {'}':'{',')':'(',']':'['}
        closing = ['}',')',']']

        i = 0
        
        while i < len(s):
            if s[i] not in closing:
                q.append(s[i])
                i += 1
            else:
                if len(q) == 0 or d[s[i]] != q.pop():
                    return False
                else:
                    i += 1
        if len(q) == 0:
            return True
        else:
            return False