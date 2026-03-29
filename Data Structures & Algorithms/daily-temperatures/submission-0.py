class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pairs of [temperature,index]
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                ans[stack_i] = i - stack_i
            stack.append([t, i])
        return ans