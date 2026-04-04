from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for val in strs:
            valmap = [0]*26
            for char in val:
                valmap[ord(char)-ord('a')] += 1
            hmap[tuple(valmap)].append(val)
        
        return [x for x in hmap.values()]