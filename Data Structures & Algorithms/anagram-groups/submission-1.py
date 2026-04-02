from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for val in strs:
            charmap = [0] * 26
            for char in val:
                charmap[ord(char) - 97] += 1

            anagramMap[tuple(charmap)].append(val)

        return list(anagramMap.values())
                