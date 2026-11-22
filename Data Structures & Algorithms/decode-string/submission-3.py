class Solution:
    def decodeString(self, s: str) -> str:
        def isChar(s):
            return ord('a') <= ord(s[0]) <= ord('z')

        def isDigit(s):
            return ord('0') <= ord(s[0]) <= ord('9')
        
        stack = []
        repeat = ""
        times = ""
        string = ""

        i = len(s) - 1
        while i >= 0:
            if s[i] == "[":
                while stack and isChar(stack[-1]):
                    repeat += stack.pop()
                stack.pop()
                
                i -= 1
                while i >= 0 and isDigit(s[i]):
                    times += s[i]
                    i -= 1
                
                times = int(times[::-1])
                for _ in range(times):
                    string += repeat
                stack.append(string)

                repeat = times = string = ""
            else:
                stack.append(s[i])
                i -= 1

        ans = ""
        for s in reversed(stack):
            ans += s
        return ans