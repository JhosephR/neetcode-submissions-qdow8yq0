class TimeMap:

    def __init__(self):
        self.timeStamp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeStamp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        vals = self.timeStamp[key]
        l, r = 0, len(vals) - 1
        while l <= r:
            m = l + (r - l) // 2
            if vals[m][1] < timestamp:
                l = m + 1
                ans = vals[m][0]
            elif vals[m][1] > timestamp:
                r = m - 1
            else:
                return vals[m][0]
        return ans