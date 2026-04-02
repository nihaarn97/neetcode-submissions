class Solution:
    def encode(self, strs):
            result = ""
            for val in strs:
                result += str(len(val)) + '#' + val
            return result

    def decode(self, s):
        result = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != '#':
                j = j + 1
            len_curr_s = int(s[i:j])
            i = j+1
            j = i + len_curr_s
            result.append(s[i:j])
            i = j
        return result
