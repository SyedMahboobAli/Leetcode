class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #we are reversing the question. We see what all indexes we can reach from pacific and atlantic
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        res = []

        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        def dfs(r,c,visited):

            visited[r][c] = True

            for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                nr,nc = r+dr, c+dc
                #This condition can't be checked on in the loop and not in dfs due to heights check. it needs two cells:nr,nc and r,c. If we want to check this is dfs, we should send one more parameter
                if 0<=nr<rows and 0<=nc<cols and not visited[nr][nc] and heights[nr][nc]>=heights[r][c]:
                    dfs(nr,nc,visited)
        
        for i in range(rows):
            if not pacific[i][0]: #these additional checks to avoid redundant dfs calls, and to improve performance
                dfs(i,0,pacific)
        for j in range(cols):
            if not pacific[0][j]:
                dfs(0,j,pacific)
        
        for i in range(rows):
            if not atlantic[i][cols-1]:
                dfs(i,cols-1,atlantic)
        for j in range(cols):
            if not atlantic[rows-1][j]:
                dfs(rows-1,j,atlantic)

        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i,j])
        
        return res
