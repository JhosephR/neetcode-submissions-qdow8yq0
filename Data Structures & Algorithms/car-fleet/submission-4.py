class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spe = sorted(zip(position, speed), reverse=True)
        timeStack = []
        
        for p, s in pos_spe:
            time = (target - p) / s
            if not timeStack:
                timeStack.append(time)
            elif time > timeStack[-1]:
                timeStack.append(time)
        return len(timeStack)