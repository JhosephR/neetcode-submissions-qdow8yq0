class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeed = sorted(zip(position, speed))
        stack = []

        for p, s in reversed(positionSpeed):
            time = (target - p) / s
            if stack and stack[-1] < time:
                stack.append(time)
            elif not stack:
                stack.append(time)
        return len(stack)