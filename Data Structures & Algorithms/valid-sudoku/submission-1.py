from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hmap_r = defaultdict(set)
        hmap_c = defaultdict(set)
        hmap_b = defaultdict(set)

        for i in range(9):
            if i%3 == 0:
                hmap_b = defaultdict(set)
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] not in hmap_r[i]) and (board[i][j] not in hmap_c[j]) and (board[i][j] not in hmap_b[i//3 + j//3]):
                    hmap_r[i].add(board[i][j])
                    hmap_c[j].add(board[i][j])
                    hmap_b[i//3 + j//3].add(board[i][j])
                else:
                    return False

        return True