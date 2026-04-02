class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            self.hashmap.append([key, value])
        else:
            for val in self.hashmap:
                if val[0] == key:
                    val[1] = value
                    break
        

    def get(self, key: int) -> int:
        for val in self.hashmap:
            if val[0] == key:
                return val[1]
        return -1

    def remove(self, key: int) -> None:
        temp = []
        for val in self.hashmap:
            if val[0] != key:
                temp.append(val)
        self.hashmap = temp


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)