class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if len(self.timeMap) == 0 or key not in self.timeMap:
            return ""

        l, r, = 0, len(self.timeMap[key]) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if self.timeMap[key][m][0] > timestamp:
                r = m - 1
            elif self.timeMap[key][m][0] < timestamp:
                l = m + 1
            else:
                return self.timeMap[key][m][1]
            
        if self.timeMap[key][m][0] > timestamp:
            m = m - 1
        
        if m >= 0 and self.timeMap[key][m][0] <= timestamp:
            return self.timeMap[key][m][1]
        else:
            return ""