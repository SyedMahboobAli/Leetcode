#DFS Solution, here the approach is using 4 dfs calls in all directions. Other approach is similar to pacific atlantic solution also present in BFS approach
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
          return 0
        count=0

        n,m=len(grid),len(grid[0])

        def dfs(r,c):
            # Check boundaries and water/visited cells
            if(r<0 or c<0 or r>=n or c>=m or grid[r][c] != '1'):
                return
            #So we are only visiting the cells that are 1
            grid[r][c]='0' # mark as visited by making it 0
            # Explore all 4 directions
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for i in range(n):
            for j in range(m):
                if(grid[i][j]=='1'): # found an unvisited land
                    count+=1
                    dfs(i,j)
                
        return count

#BFS Solution

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count=0
        n,m=len(grid),len(grid[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        def bfs(r,c):
            q=deque()
            q.append((r,c))
            grid[r][c]='0' # marking as visited
            while q:
                x,y=q.popleft()
                for dr,dc in directions:
                    nr,nc=dr+x,dc+y
                    if(0<=nr<n and 0<=nc<m and grid[nr][nc]=='1'):
                        grid[nr][nc]='0'
                        q.append((nr,nc))
 
        for i in range(n):
            for j in range(m):
                if(grid[i][j]=='1'): # found an unvisited land
                    count+=1
                    bfs(i,j)
                
        return count
