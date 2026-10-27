class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p):
            return p[0]**2 + p[1]**2

        def partition(left, right):
            pivot = distance(points[r])
            i = left

            for j in range(left, right):
                if distance(points[j]) <= pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[right] = points[right], points[i]
            return i
        
        l, r = 0, len(points) - 1

        while l <= r:
            p = partition(l, r)
            if p < k:
                l = p + 1
            elif p > k:
                r = p - 1
            else:
                break
        return points[:k]