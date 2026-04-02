class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        res = ""
        i = 0
        while i<len(strs[0]) and i<len(strs[-1]): 
            if strs[0][i] == strs[-1][i]:
                res = res + strs[0][i]
                i = i+1
            else:
                break
        return res
        