class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mAp = {'}':'{', ']':'[', ')':'('}

        for c in s:
            if c not in mAp:
                stack.append(c)
                continue
            if not stack or stack[-1] != mAp[c]:
                return False
            stack.pop()

        return not stack