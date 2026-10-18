class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            freq[t] = 1 + freq.get(t, 0)
        
        maxHeap = []
        for v, f in freq.items():
            heapq.heappush(maxHeap, -f)

        time = 0
        q = deque()     # [frequency, idle time/ target time]
        while maxHeap or q:
            time += 1
            if maxHeap:
                f = 1 + heapq.heappop(maxHeap)
                if f:
                    q.append([f, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time