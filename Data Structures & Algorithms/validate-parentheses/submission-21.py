class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {')':'(', '}':'{',']':'['}
        stack = []

        for c in s:
            if stack and c in parenthesis:
                if stack[-1] == parenthesis[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0