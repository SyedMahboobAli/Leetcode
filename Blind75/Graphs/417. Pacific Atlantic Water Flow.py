class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # We are going to move from the borders to every cell instead of cell to border ocean
        # Edge case: empty grid
        if not heights or not heights[0]:
            return []

        n,m=len(heights),len(heights[0])

        # Boolean matrices to track reachability from each ocean
        pacific=[[False]*m for _ in range(n)]
        atlantic=[[False]*m for _ in range(n)]

        # 4 possible directions (up, down, left, right)
        directions=[[-1,0],[0,1],[1,0],[0,-1]]

        # DFS to mark reachable cells
        def dfs(r,c,visited):
            visited[r][c]=True
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                # Move to next cell if it's higher or equal and not yet visited
                if(0<=nr<n and 0<=nc<m and not visited[nr][nc] and heights[nr][nc]>=heights[r][c]):
                    dfs(nr,nc,visited)
        # Start DFS from Pacific edges          
        for i in range(n):
            dfs(i,0,pacific) # left column
        for j in range(m):
            dfs(0,j,pacific) # top row
        
        # Start DFS from Atlantic edges
        for i in range(n):
            dfs(i,m-1,atlantic) # right column
        for j in range(m):
            dfs(n-1,j,atlantic) # bottom row
        
        result=[]
        # Cells reachable from both oceans
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i,j])
        
        return result

        
