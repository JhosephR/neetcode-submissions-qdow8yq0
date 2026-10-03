class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            heapq.heappush(maxHeap, [-(x**2 + y**2)**0.5, x,y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        ans = []
        for d, x, y in maxHeap:
            ans.append([x,y])
        return ans