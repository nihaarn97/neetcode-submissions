from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hmap_r = defaultdict(set)
        hmap_c = defaultdict(set)
        hmap_b = defaultdict(set)

        for i in range(9):
            if i%3==0:
                hmap_b = defaultdict(set)
            for j in range(9):
                if board[i][j].isdigit():
                    num = int(board[i][j])
                    if (num in hmap_r[i]) or (num in hmap_c[j]) or (num in hmap_b[i//3+j//3]):
                        return False
                    hmap_r[i].add(num)
                    hmap_c[j].add(num)
                    hmap_b[i//3+j//3].add(num)
                else:
                    continue

        return True