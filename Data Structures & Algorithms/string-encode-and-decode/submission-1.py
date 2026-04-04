class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for val in strs:
            res += str(len(val)) + '#' + val
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j = i
            while s[j]!='#':
                j = j+1
            
            str_len = int(s[i:j])
            i = j+1
            res.append(s[i:i+str_len])
            i = i+str_len

        return res