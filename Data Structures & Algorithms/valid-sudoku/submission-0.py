from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hmap_rows = defaultdict(list)
        hmap_cols = defaultdict(list)
        hmap_squares = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                else:
                    if board[i][j] in hmap_rows[i] or board[i][j] in hmap_cols[j] or board[i][j] in hmap_squares[(i//3, j//3)]:
                        return False
                    hmap_rows[i].append(board[i][j])
                    hmap_cols[j].append(board[i][j])
                    hmap_squares[(i//3, j//3)].append(board[i][j])
        
        return True


        