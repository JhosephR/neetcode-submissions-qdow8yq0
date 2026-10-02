class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x, y in points:
            heapq.heappush(maxheap, [-(x**2 + y**2), x, y])
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        
        ans = []
        for d, x, y in maxheap:
            ans.append([x,y])
        return ans