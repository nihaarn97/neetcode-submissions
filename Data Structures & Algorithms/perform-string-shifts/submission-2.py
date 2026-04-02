class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        pos = 0
        for val in shift:
            if val[0] == 0:
                pos -= val[1]
            else:
                pos += val[1]
        
        if pos == 0:
            return s
        elif pos > 0:
            pos = pos%len(s)
            return s[len(s)-pos:] + s[:len(s)-pos]
        else:
            pos = abs(pos)%len(s)
            return s[pos:] + s[:pos]