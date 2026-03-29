import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}

        for token in tokens:
            if token in operators:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(operators[token](n2, n1)))
            else:
                stack.append(int(token))
        return stack[0]