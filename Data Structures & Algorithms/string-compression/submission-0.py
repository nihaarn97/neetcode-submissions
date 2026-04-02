class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        res = ""
        while i < len(chars):
            curr = chars[i]
            count = 0
            while i<len(chars) and chars[i]==curr:
                count = count+1
                i = i+1
            
            if count == 1:
                chars[j] = curr
                j = j+1
            else:
                chars[j] = curr
                j = j+1
                for val in str(count):
                    chars[j] = val
                    j = j+1

        return j
        