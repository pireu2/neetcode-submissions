class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.timemap:
            return ""

        values = self.timemap[key]

        l = 0
        r = len(values) - 1
        res = [-1, ""]

        while l <= r:
            mid = (l + r) // 2

            if values[mid][0] == timestamp:
                return values[mid][1]
            
            if values[mid][0] > res[0] and values[mid][0] <= timestamp:
                res[0] = values[mid][0]
                res[1] = values[mid][1]

            if timestamp < values[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        return res[1]
