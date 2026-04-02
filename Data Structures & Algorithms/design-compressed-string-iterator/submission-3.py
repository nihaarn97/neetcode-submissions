class StringIterator:

    def __init__(self, compressedString: str):
        self.chrs = []
        self.nums = []
        char = ""
        i = 0
        while i<len(compressedString):
            if not compressedString[i].isdigit():
                char = compressedString[i]
                i = i+1
            else:
                j = i
                num = 0
                while j<len(compressedString) and compressedString[j].isdigit():
                    num = num*10 + int(compressedString[j])
                    j = j+1
                
                self.chrs.append(char)
                self.nums.append(num)
                i = j

        self.ptr = 0
            

    def next(self) -> str:
        if self.ptr < len(self.nums):
            char = self.chrs[self.ptr]
            self.nums[self.ptr] -= 1
            if self.nums[self.ptr] == 0:
                self.ptr += 1
            return char
        else:
            return ' '

    def hasNext(self) -> bool:
        if self.ptr == len(self.chrs):
            return False
        return True


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
