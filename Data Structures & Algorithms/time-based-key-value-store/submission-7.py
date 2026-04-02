class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {timestamp: value}
        else:
            self.store[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            timestamps = list(self.store[key].keys())
            low = 0
            high = len(timestamps) - 1
            res = ""
            while low<=high:
                mid = (low+high)//2
                if timestamps[mid] <= timestamp:
                    res = self.store[key][timestamps[mid]]
                    low = mid + 1
                else:
                    high = mid - 1

            return res
        else:
            return ""