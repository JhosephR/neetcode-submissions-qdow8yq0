class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = lambda x: x[0]**2 + x[1]**2
        def twoWayPartition(l, r):
            low = l
            p = l   # pointer
            pivot = distance(points[r])

            while p < r:
                if distance(points[p]) <= pivot:
                    points[p], points[low] = points[low], points[p]
                    low += 1
                p += 1
            points[low], points[r] = points[r], points[low]
            return low
        
        left, right = 0, len(points) - 1
        partition_point = len(points)
        
        while partition_point != k:
            partition_point = twoWayPartition(left, right)
            if partition_point < k:
                left = partition_point + 1
            else:
                right = partition_point - 1
        return points[:k]