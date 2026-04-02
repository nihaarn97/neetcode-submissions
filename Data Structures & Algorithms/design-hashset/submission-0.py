class MyHashSet:

    def __init__(self):
        self.hashset = []
        
    def add(self, key: int) -> None:
        self.hashset.append(key)
        return None

    def remove(self, key: int) -> None:
        temp = []
        for val in self.hashset:
            if val!=key:
                temp.append(val)

        self.hashset = temp

    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)