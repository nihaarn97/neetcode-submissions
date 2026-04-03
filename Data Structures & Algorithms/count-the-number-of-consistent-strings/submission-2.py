class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        chars = set(allowed)
        count = 0
        for word in words:
            flag = 0
            for char in word:
                if char not in chars:
                    flag = 1
                    break
                
            if flag == 0:
                count = count+1
        
        return count