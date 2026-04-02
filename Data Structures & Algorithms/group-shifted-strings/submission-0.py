from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def gethash(string):
            key = []
            for a,b in zip(string, string[1:]):
                key.append(chr((ord(b)-ord(a))%26 + ord('a')))
            return "".join(key)

        groups = defaultdict(list)
        for val in strings:
            groups[gethash(val)].append(val)

        return list(groups.values())