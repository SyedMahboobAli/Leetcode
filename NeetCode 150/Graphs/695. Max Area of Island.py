class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
        
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r,c):

            if r<0 or r>=rows or c<0 or c>= cols or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0
            area = 1
            
            for dr, dc in ((0,1),(0,-1),(1,0),(-1,0)):
                nr, nc = r + dr, c + dc
                area += dfs(nr,nc)
            
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area,dfs(i,j))
        
        return max_area
