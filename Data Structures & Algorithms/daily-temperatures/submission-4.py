class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #[index, temperature]
        ans = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                i_stack, t_stack = stack.pop()
                ans[i_stack] = i - i_stack
            stack.append([i, v])
        return ans