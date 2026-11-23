class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                subString = ""
                while stack and stack[-1] != "[":
                    subString = stack.pop() + subString
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(subString * int(k))
        return "".join(stack)