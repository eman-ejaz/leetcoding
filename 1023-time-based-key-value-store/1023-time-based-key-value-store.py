class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        keys = self.map.get(key, [])
        keys.append([value, timestamp])
        self.map[key] = keys

    def get(self, key: str, timestamp: int) -> str:
        keys = self.map.get(key, [])

        l, r = 0, len(keys) - 1

        while l <= r:
            m = (l + r) // 2

            midKey = keys[m]
            if midKey[1] == timestamp:
                return midKey[0]

            elif midKey[1] > timestamp:
                r = m - 1
            else:
                l = m + 1

        if r < 0: 
            return ""
        return keys[r][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)