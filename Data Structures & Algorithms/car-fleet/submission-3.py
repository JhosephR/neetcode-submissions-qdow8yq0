class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
 
        for i, (p, s) in enumerate(cars):
            time_taken = (target - p) / s
            if i == 0:
                stack.append(time_taken)
            elif stack and time_taken > stack[-1]:
                stack.append(time_taken)
        return len(stack)