class Solution:
    def isValid(self, s: str) -> bool:
        closing_p = {")":"(", "}":"{", "]":"["}
        stack = []
        for c in s:
            print(stack)
            if stack and c in closing_p:
                if stack[-1] == closing_p[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0