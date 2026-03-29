import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}

        for e in tokens:
            if e in operators:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(operators[e](n2, n1)))
            else:
                stack.append(int(e))
        return stack[-1]