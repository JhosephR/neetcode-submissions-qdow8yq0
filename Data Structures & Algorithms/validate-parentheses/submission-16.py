class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {")":"(", "]":"[", "}":"{"}
        stack = []

        for c in s:
            if c in parentheses:
                if len(stack) and stack[-1] == parentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0