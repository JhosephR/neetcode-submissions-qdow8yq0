class KthLargest:   # overal - O(n*logk+m*logk) = O((n+m)*logk) = O(m*logk) where m >> n
                    # where m in the number of calls to add()
    def __init__(self, k: int, nums: List[int]): # overal - O(n*logk)
        self.heap, self.k = [], k
        for n in nums:                      # O(n) - loops n times
            heapq.heappush(self.heap, n)    # O(logk) - heap size is around k
            if len(self.heap) > k:          # O(1) - length check is constant time
                heapq.heappop(self.heap)    # O(logk) - heap size is around k

    def add(self, val: int) -> int:             # overal - O(logk)
        heapq.heappush(self.heap, val)      # O(logk) - heap size is around k
        if len(self.heap) > self.k:         # O(1) - length check is constant time
            heapq.heappop(self.heap)        # O(logk) - heap size is around k
        return self.heap[0]                 # O(1) - peek smallest element is constant time