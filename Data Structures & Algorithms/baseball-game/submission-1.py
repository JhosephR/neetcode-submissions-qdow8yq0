class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, sm = [], 0
        for o in operations:
            if o == "+":
                sm += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif o == "D":
                sm += stack[-1] * 2
                stack.append(stack[-1] * 2)
            elif o == "C":
                sm -= stack[-1]
                stack.pop()
            else:
                sm += int(o)
                stack.append(int(o))
        return sm