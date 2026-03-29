class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = sorted(zip(position, speed), reverse=True)
        stack = []
 

        for i, (p, s) in enumerate(position_speed):
            time = (target - p) / s
            if i == 0:
                stack.append(time)
            elif stack and time > stack[-1]:
                stack.append(time)
        return len(stack)