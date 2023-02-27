class TimeMap:

    def __init__(self):
        self.tmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap.keys():
            self.tmap[key] = []
        self.tmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans, values = "", self.tmap.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            i = (l+r) // 2
            if values[i][1] <= timestamp:
                ans = values[i][0]
                l = i + 1
            else:
                r = i - 1
        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)