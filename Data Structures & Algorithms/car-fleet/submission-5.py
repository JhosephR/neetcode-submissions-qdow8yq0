class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeed = sorted(zip(position, speed))
        stack = []
        
        for p, s in reversed(positionSpeed):
            t = (target - p) / s
            if stack and t > stack[-1]:
                    stack.append(t)
            elif not stack:
                stack.append(t)
        return len(stack)