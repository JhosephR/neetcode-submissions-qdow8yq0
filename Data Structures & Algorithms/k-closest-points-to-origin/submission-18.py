class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p):
            return p[0]**2 + p[1]**2

        def partition(left, right):
            pivot = distance(points[right])
            i = left

            for j in range(left, right):
                if distance(points[j]) <= pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[right] = points[right], points[i]
            return i
        
        l, r = 0, len(points) - 1
        index = len(points)

        while l <= r:
            index = partition(l, r)
            if index < k:
                l = index + 1
            elif index > k:
                r = index - 1
            else:
                break
        return points[:k]