class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:        
        rows,cols = len(grid), len(grid[0])
        q = deque()
        minutes = 0 #this is 0 indexed, so return minutes - 1 at the end
        fresh = 0
        # Step 1: count fresh oranges & enqueue rotten ones
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        # No fresh oranges
        if fresh == 0:
            return 0
        # Step 2: BFS
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            minutes += 1
        # Step 3: check if all fresh are rotten
        return minutes - 1 if fresh == 0 else -1
            


