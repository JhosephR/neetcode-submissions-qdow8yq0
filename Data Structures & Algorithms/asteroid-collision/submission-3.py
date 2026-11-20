class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:  # if colliding
                if abs(a) > abs(stack[-1]):           # destroy smaller one in stack
                    stack.pop()
                    continue                          # check next in stack
                elif abs(a) == abs(stack[-1]):        # destroy both if same size
                    stack.pop() 
                break                                 # incoming asteroid was destroyed
            else:
                stack.append(a)                       # not collision or all asteroids were destroyed
        return stack