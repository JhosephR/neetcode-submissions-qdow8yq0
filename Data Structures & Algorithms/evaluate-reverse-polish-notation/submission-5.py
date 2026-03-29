import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}
        stack = []

        for c in tokens:
            if c in operators:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(operators[c](n2, n1)))
            else:
                stack.append(int(c))
        return stack[0]