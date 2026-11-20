class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0: # colliding (> <) asteroids instead of (< >)
                if abs(asteroid) > abs(stack[-1]):  # destroy smaller ones than incoming asteroid
                    stack.pop()
                    continue                        # check left over asteroids
                elif abs(asteroid) == abs(stack[-1]):   # same size
                    stack.pop()
                break                               # incoming asteroid was destroyed
            else:
                stack.append(asteroid) # add asteroid if no collision or all asteroids were destroyed
        return stack