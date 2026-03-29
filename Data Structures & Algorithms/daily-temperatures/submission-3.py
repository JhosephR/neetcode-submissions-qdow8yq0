class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexStack = []
        ans = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while indexStack and temperatures[indexStack[-1]] < v:
                i_stack = indexStack.pop()
                ans[i_stack] = i - i_stack
            indexStack.append(i)
        return ans