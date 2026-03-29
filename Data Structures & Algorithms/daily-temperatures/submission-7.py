class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, ans = [], [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                ans[stack_i] = i - stack_i
            stack.append([t, i])
        return ans