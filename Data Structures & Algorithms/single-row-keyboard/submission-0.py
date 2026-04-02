class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hmap = {}
        for idx, val in enumerate(keyboard):
            hmap[val] = idx
        
        time = hmap[word[0]]

        for i in range(1, len(word)):
            time += abs(hmap[word[i]] - hmap[word[i-1]])

        return time