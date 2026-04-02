class StringIterator:

    def __init__(self, compressedString: str):
        self.unc = ""
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
                
                self.unc += char*num
                i = j

        self.pos = -1

    def next(self) -> str:
        self.pos += 1
        return self.unc[self.pos]

    def hasNext(self) -> bool:
        if self.pos == len(self.unc)-1:
            return False
        return True


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
