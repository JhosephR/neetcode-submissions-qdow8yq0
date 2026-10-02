class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for p in points:
            x, y = p
            heapq.heappush(maxheap, (-math.sqrt(x**2 + y**2),p))
        
        while len(maxheap) > k:
            heapq.heappop(maxheap)
        
        ans = []
        for t in maxheap:
            ans.append(t[1])
        return ans