class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        values = self.timeMap[key]
        if len(values) == 0:
            return ans

        l, r = 0, len(values) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if values[m][1] < timestamp:
                ans = values[m][0]
                l = m + 1
            elif values[m][1] > timestamp:
                r = m - 1
            else:
                return values[m][0]
        
        return ans