class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        fresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))

        length = 0

        while q and fresh>0:
            for i in range(len(q)):
                curr_row, curr_col = q.popleft()

                neighbours = [[0,1], [1,0], [0,-1], [-1,0]]
                
                for dr, dc in neighbours:
                    nr, nc = curr_row + dr, curr_col + dc
                    if nr<0 or nc<0 or nr==ROWS or nc==COLS or grid[nr][nc]==0 or (nr,nc) in visited:
                        continue

                    q.append((nr,nc))
                    visited.add((nr, nc)) # So that later iterations dont end up adding this again
                    fresh = fresh - 1
            
            length += 1

        return length if fresh==0 else -1
