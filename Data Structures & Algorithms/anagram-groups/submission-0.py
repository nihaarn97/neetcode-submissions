class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for val in strs:
            charmap = [0] * 26
            for char in val:
                charmap[ord(char.lower())-ord('a')] += 1
            if tuple(charmap) in hashmap:
                hashmap[tuple(charmap)].append(val)
            else:
                hashmap[tuple(charmap)] = [val]

        return list(hashmap.values())
        