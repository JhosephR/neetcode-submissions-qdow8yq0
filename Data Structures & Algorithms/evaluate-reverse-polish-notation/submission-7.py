import operator as op
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+":op.add, "-":op.sub, "*":op.mul, "/":op.truediv}
        stack = []

        for c in tokens:
            if stack and c in operators:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(operators[c](n2, n1)))
            else:
                stack.append(int(c))
        return stack[-1]