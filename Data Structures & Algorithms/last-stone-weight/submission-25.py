class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)

        for s in stones:
            bucket[s] += 1

        x = y = maxStone
        while x > 0:
            if bucket[x] % 2 == 0:
                x -= 1
                continue
            
            nextStone = min(x - 1, y)
            while nextStone > 0 and bucket[nextStone] == 0:
                nextStone -= 1
            
            if nextStone == 0:
                return x
            
            y = nextStone
            bucket[x] -= 1
            bucket[y] -= 1
            bucket[x - y] += 1
            x = max(x - y, y)
        return x