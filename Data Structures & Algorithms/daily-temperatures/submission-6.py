class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] # pairs of [index, value]

        for curr_i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                index, temp = stack.pop()
                ans[index] = curr_i - index
            stack.append([curr_i, t])
                   
        return ans