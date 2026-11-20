class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == "+":
                stack.append(str(int(stack[-1]) + int(stack[-2])))
            elif operations[i] == "D":
                stack.append(str(int(stack[-1]) * 2))
            elif operations[i] == "C":
                stack.pop()
            else:
                stack.append(operations[i])

        sm = 0
        for n in stack:
            sm += int(n)
        return sm