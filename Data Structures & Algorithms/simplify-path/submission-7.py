class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")

        for s in paths:
            if s == "..":
                if stack:
                    stack.pop()
            elif s != "" and s != ".":
                stack.append(s)

        print(paths)
        return "/" + "/".join(stack)