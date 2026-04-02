class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        temp = self.keyStore.get(key, [])
        l = 0
        r = len(temp)-1
        while l<=r:
            mid = (l+r)//2
            if temp[mid][1] <= timestamp:
                res = temp[mid][0]
                l = mid+1
            else:
                r = mid-1

        return res

        
