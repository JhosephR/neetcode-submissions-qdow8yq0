class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        
        for path in paths:
            if path == "..":
                if stack:
                    stack.pop()
            elif path != "" and path != ".":
                stack.append(path)
        return "/" + "/".join(stack)