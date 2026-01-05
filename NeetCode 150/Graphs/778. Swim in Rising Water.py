class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        # (time, row, col)
        minHeap = [(grid[0][0],0,0)]

        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            # reached destination
            if r == n-1 and c == n-1:
                return time
            
            if (r,c) in visited:
                continue
            visited.add((r,c))

            for dr,dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                    next_time = max(time,grid[nr][nc])
                    heapq.heappush(minHeap,(next_time,nr,nc))

