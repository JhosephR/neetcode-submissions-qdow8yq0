class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        file = ""
        for c in path + "/":
            if c == "/":
                if file == "..":
                    if stack:
                        stack.pop()
                elif file != "" and file != ".":
                    stack.append(file)
                file = ""
            else:
                file += c
        return "/" + "/".join(stack)