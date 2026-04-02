from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1)!=len(sentence2):
            return False

        if len(sentence1) == len(sentence2) == 1:
            return True

        hmap = defaultdict(list)
        for val in similarPairs:
            hmap[val[0]].append(val[1])
            hmap[val[1]].append(val[0])

        print(hmap)
        
        for i in range(len(sentence1)):
            if sentence2[i] in hmap[sentence1[i]]:
                continue
            elif sentence1[i] == sentence2[i]:
                continue
            return False

        return True