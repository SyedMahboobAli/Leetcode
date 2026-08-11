class Solution {
    public int swimInWater(int[][] grid) {
        //the question is maximum height along the path, since you can only enter if time >= height

        int n = grid.length;

        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        pq.offer(new int[]{grid[0][0],0,0});

        boolean[][] visited = new boolean[n][n];

        int[][] directions = {{0,1},{0,-1},{1,0},{-1,0}};
        //min heap is used to always expand the cell with minimum/smallest possible current time
        while(!pq.isEmpty()){
            int[] curr = pq.poll();
            int time = curr[0];
            int r = curr[1];
            int c = curr[2];

            if(visited[r][c])
                continue;
            
            visited[r][c] = true;

            if(r == n-1 && c == n-1)
                return time;
            
            for(int[] dir: directions){
                int dr = dir[0];
                int dc = dir[1];
                int nr = r + dr;
                int nc = c + dc;

                if(nr >= 0 && nr < n && nc >=0 && nc< n && !visited[nr][nc]){
                    // path cost becomes the maximum height so far, the last time can also be like 1, and then 1 will be returned so,
                    int nextTime= Math.max(time,grid[nr][nc]);
                    pq.offer(new int[]{nextTime,nr,nc});
                }
            }
        }

    return -1;

    }
}
