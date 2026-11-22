class Solution:
    def decodeString(self, s: str) -> str:

        def isDigit(c):
            return ord('0') <= ord(c[0]) <= ord('9')

        stack = []

        for c in s:
            if c == "]":
                subString = ""
                while stack[-1] != "[":
                    subString = stack.pop() + subString
                stack.pop()

                k = ""
                while stack and isDigit(stack[-1]):
                    k = stack.pop() + k
                
                stack.append(subString * int(k))
            else:
                stack.append(c)
        return "".join(stack)