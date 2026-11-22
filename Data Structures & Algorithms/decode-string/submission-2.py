class Solution:
    def decodeString(self, s: str) -> str:

        def isDigit(c):
            return ord('0') <= ord(c[0]) <= ord('9')

        def isChar(c):
            return ord('a') <= ord(c[0]) <= ord('z')

        stack = []
        repeat = ""
        times = ""
        string = ""

        for c in s:
            if c == "]":
                while stack and not isDigit(stack[-1]):
                    if stack[-1][0] == "[":
                        stack.pop()
                        continue
                    repeat += stack.pop()
                while stack and not isChar(stack[-1]):
                    if stack[-1][0] == "[":
                        stack.pop()
                        break
                    times += stack.pop() 
                
                times = times[::-1]
                for _ in range(int(times)):
                    string += repeat
                stack.append(string)
                
                repeat = ""
                times = ""
                string = ""
            else:
                stack.append(c)
        print(stack)
        ans = ""
        for s in stack:
            ans += s[::-1]
        return ans