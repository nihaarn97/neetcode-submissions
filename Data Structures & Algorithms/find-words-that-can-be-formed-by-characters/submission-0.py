class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c1 = Counter(chars)
        res = 0
        for val in words:
            c2 = Counter(val)
            if not c2-c1:
                res += len(val)

        return res
