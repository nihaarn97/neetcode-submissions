class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        
        hmap = {}
        visited = set()
        for char, word in zip(pattern, s):
            if char in hmap:
                if hmap[char] != word:
                    return False
            else:
                if word in visited:
                    return False
                else:
                    hmap[char] = word
                    visited.add(word)

        return True
        