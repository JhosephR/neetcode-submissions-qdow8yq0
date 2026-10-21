class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)
        for s in stones:
            bucket[s] += 1

        first = second = maxStone
        while first > 0:
            if bucket[first] % 2 == 0:
                first -= 1
                continue

            nextStone = min(first - 1, second)
            while nextStone > 0 and bucket[nextStone] == 0:
                nextStone -= 1

            if nextStone == 0:
                return first
            
            second = nextStone
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1
            first = max(first - second, second)
        return first