class Solution:
    def isValid(self, s: str) -> bool:
        closed_brackets = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in closed_brackets:
                if stack and stack[-1] == closed_brackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0