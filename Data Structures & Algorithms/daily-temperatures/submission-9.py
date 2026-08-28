class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for temp_i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[temp_i]:
                stack_i = stack.pop()
                ans[stack_i] = temp_i - stack_i
            stack.append(temp_i)
        return ans